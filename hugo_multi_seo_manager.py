import os
import re
import json
import argparse
from pathlib import Path
import whisper
from google import genai
from google.genai import types

# =====================================================================
# CONFIGURATION GÉNÉRALE
# =====================================================================
GEMINI_MODEL = "gemini-2.5-flash" 
BASE_CONTENT_DIR = "./content"  # Racine de ton dossier de contenu Hugo
INDEX_FILE_NAME = ".series_index.json"
# =====================================================================

def transcribe_video(video_path, model_name="base"):
    """Transcrit la vidéo directement via Whisper"""
    print(f"🎬 Analyse et transcription de la vidéo : {video_path.name}...")
    model = whisper.load_model(model_name)
    result = model.transcribe(str(video_path), language="fr")
    return result["text"]

def generate_hugo_article(transcript, episode_num, engine, series_slug, category):
    """Demande à l'IA de générer l'article brut selon tes directives strictes"""
    print(f"✍️  Génération de l'article ({category}) pour {engine} via Gemini...")
    client = genai.Client()
    
    system_instruction = (
        f"Tu es un rédacteur web expert en Game Development. Ton but est de transformer "
        f"une transcription brute de tutoriel vidéo portant sur le moteur/langage '{engine}' en un article de blog.\n\n"
        "Tu dois STRICTEMENT respecter les consignes d'ordonnancement suivantes :\n"
        "1. Commence DIRECTEMENT le fichier par le Front Matter YAML entouré de '---'. Ne mets rien avant.\n"
        f"2. Dans le Front Matter, inclus uniquement : title, date (AAAA-MM-JJ), categories: ['{category}'], et tags.\n"
        "3. Ne mets AUCUN champ 'prev_url', 'next_url' ou 'weight' dans ton Front Matter, le script s'en charge.\n"
        "4. JUSTE APRÈS le Front Matter (après le deuxième '---'), écris une ligne d'introduction adaptée au contenu.\n"
        "5. Ajoute ensuite le shortcode vidéo : {{< youtube-rgpd \"\" >}}.\n"
        "6. Propose un résumé structuré avec des listes à puces des notions clés.\n"
        f"7. Rédige une section '### Ce qui reste d'actualité aujourd'hui' pour valoriser ces concepts liés à {engine}.\n"
        "8. Termine le markdown avec le shortcode : {{< footer >}}.\n"
        "9. TOUT À LA FIN du document, sur une ligne isolée et en dehors du markdown, écris exactement : "
        "'SEO_SLUG: ton-titre-optimise-sans-le-mot-episode-ni-numero'"
    )
    
    prompt = f"Voici la transcription brute de l'épisode {episode_num} :\n\"\"\"\n{transcript}\n\"\"\""
    
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3
        )
    )
    return response.text

def create_chapter_index_if_missing(target_dir, series_name, engine_name):
    """Crée la page d'accueil de chapitre (_index.md) propre à l'architecture Hugo"""
    index_path = target_dir / "_index.md"
    if index_path.exists():
        return
        
    print(f"📁 Nouvelle série détectée ! Création de la page chapitre : {index_path.name}")
    clean_title = series_name.replace("-", " ").title()
    
    chapter_content = f"""---
title: "{clean_title} ({engine_name})"
archetype: "chapter"
---

Bienvenue dans la série de tutoriels consacrée à **{clean_title}** développée sur **{engine_name}**. 

Vous trouverez ci-dessous l'ensemble des chapitres, classés par ordre de progression. Utilisez les boutons de navigation pour passer d'un épisode à l'autre.
"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(chapter_content)

def load_index(index_path):
    """Charge l'index local de la série (Épisode <-> Slug)"""
    if index_path.exists():
        with open(index_path, "r", encoding="utf-8") as f:
            try:
                return {int(k): v for k, v in json.load(f).items()}
            except json.JSONDecodeError:
                return {}
    return {}

def save_index(index, index_path):
    """Sauvegarde l'index de la série"""
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=4)

def rewrite_front_matter_links(file_path, base_url_path, ep_num, prev_slug, next_slug):
    """Nettoie le fichier et injecte le titre formaté, le weight et le maillage sans regex fragiles"""
    if not file_path.exists():
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Sécurité début de fichier
    if not content.startswith("---"):
        try:
            content = re.sub(r"^[\s\S]*?(---\n)", r"\1", content)
        except Exception:
            # Si même ça, ça plante, on cherche manuellement le premier index du Front Matter
            idx = content.find("---")
            if idx != -1:
                content = content[idx:]

    # Extraction native du titre (sans regex)
    clean_title = "Tutoriel"
    for line in content.splitlines():
        if line.startswith("title:"):
            raw_title = line.replace("title:", "", 1).strip()
            clean_title = raw_title.strip('"').strip("'")
            # Nettoyage simple des prefixes de numéros (ex: "Ep 12 - ", "05. ")
            clean_title = clean_title.split(":", 1)[-1].split("-", 1)[-1].strip()
            break

    # Nettoyage des anciennes lignes de Front Matter (Ligne par ligne, ultra safe)
    lines = content.splitlines()
    filtered_lines = []
    for line in lines:
        if any(line.startswith(k) for k in ["title:", "weight:", "prev_url:", "next_url:"]):
            continue
        filtered_lines.append(line)
    
    # On reconstruit le contenu sans ces lignes
    content_without_meta = "\n".join(filtered_lines)
    
    # Reconstruction propre du bloc de métadonnées
    meta_lines = f'title: "{ep_num}. {clean_title}"\n'
    meta_lines += f'weight: {ep_num}\n'
    if prev_slug:
        meta_lines += f'prev_url: "{base_url_path}/{prev_slug}/"\n'
    if next_slug:
        meta_lines += f'next_url: "{base_url_path}/{next_slug}/"\n'
    
    # Injection juste après les trois premiers tirets du fichier
    if content_without_meta.startswith("---"):
        updated_content = content_without_meta.replace("---\n", f"---\n{meta_lines}", 1)
    else:
        updated_content = f"---\n{meta_lines}---\n{content_without_meta}"
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

def main():
    parser = argparse.ArgumentParser(description="Pipeline Markdown Hugo - Catégories dynamiques")
    parser.add_argument("--video", required=True, help="Fichier vidéo brute")
    parser.add_argument("--ep", required=True, type=int, help="Numéro de l'épisode")
    parser.add_argument("--engine", required=True, help="Moteur ou langage (ex: 'GDevelop 5')")
    parser.add_argument("--series", required=True, help="Nom de la série/dossier (ex: 'sweet-void')")
    parser.add_argument("--category", required=True, help="Catégorie Hugo (ex: 'Archive', 'Tutoriel', 'Devlog')")
    args = parser.parse_args()
    
    video_path = Path(args.video)
    
    # Normalisation du nom du moteur pour l'arborescence
    engine_slug = re.sub(r'[^a-zA-Z0-9]', '-', args.engine.lower())
    engine_slug = re.sub(r'-+', '-', engine_slug).strip('-')
    
    # Détermination des chemins
    target_dir = Path(BASE_CONTENT_DIR) / engine_slug / args.series
    base_url_path = f"/{engine_slug}/{args.series}"
    index_path = target_dir / INDEX_FILE_NAME
    
    if not video_path.exists():
        print(f"❌ Fichier vidéo introuvable : {video_path}")
        return

    # 1. Transcription Whisper
    transcript = transcribe_video(video_path)
    
    # 2. Rédaction Gemini avec la catégorie passée en paramètre
    raw_article = generate_hugo_article(transcript, args.ep, args.engine, args.series, args.category)
    
    # 3. Extraction du slug SEO
    slug_match = re.search(r"SEO_SLUG:\s*([a-zA-Z0-9-_]+)", raw_article)
    if slug_match:
        current_slug = slug_match.group(1).strip()
        clean_markdown = re.sub(r"SEO_SLUG:.*", "", raw_article).strip()
    else:
        print("⚠️ Aucun slug SEO détecté. Utilisation d'un fallback numéro.")
        current_slug = f"episode-{args.ep}"
        clean_markdown = raw_article

    # 4. Création des répertoires et du _index.md de type chapitre si manquant
    target_dir.mkdir(parents=True, exist_ok=True)
    create_chapter_index_if_missing(target_dir, args.series, args.engine)

    # 5. Enregistrement dans l'index de la série
    series_index = load_index(index_path)
    series_index[args.ep] = current_slug
    save_index(series_index, index_path)

    # 6. Écriture initiale de l'épisode (.md)
    current_file_path = target_dir / f"{current_slug}.md"
    with open(current_file_path, "w", encoding="utf-8") as f:
        f.write(clean_markdown)

    # 7. Formatage final des Front Matters (Titre, Weight, Maillage)
    print(f"🔗 Formatage et maillage SEO pour la série '{args.series}'...")
    for ep_num, slug in series_index.items():
        file_path = target_dir / f"{slug}.md"
        
        prev_slug = series_index.get(ep_num - 1, "index")
        next_slug = series_index.get(ep_num + 1, None)
        
        rewrite_front_matter_links(file_path, base_url_path, ep_num, prev_slug, next_slug)

    print(f"💾 Terminé ! Contenu généré et indexé avec succès dans : {target_dir}")

if __name__ == "__main__":
    main()