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
BASE_CONTENT_DIR = "./content"
INDEX_FILE_NAME = ".series_index.json"
SUPPORTED_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".mp3", ".m4a"}
# =====================================================================

def extract_episode_number(filename):
    """
    Extrait le premier nombre trouvé dans le nom du fichier pour déterminer l'épisode.
    Exemples : "tuto_01.mp4" -> 1, "05-menu.mp4" -> 5, "episode3.mp4" -> 3
    """
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    return None

def transcribe_video(video_path, whisper_model):
    """Transcrit la vidéo directement via l'instance Whisper partagée"""
    print(f"\n🎬 [Whisper] Analyse et transcription : {video_path.name}...")
    result = whisper_model.transcribe(str(video_path), language="fr")
    return result["text"]

def generate_hugo_article(transcript, episode_num, engine, series_slug, category):
    """Demande à l'IA de générer l'article brut selon tes directives strictes"""
    print(f"✍️  [Gemini] Génération de l'article ({category}) pour l'épisode {episode_num}...")
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
    """Charge l'index local de la série"""
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
    """Nettoie le fichier et injecte le titre formaté, le weight et le maillage sans plantage regex"""
    if not file_path.exists():
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if not content.startswith("---"):
        idx = content.find("---")
        if idx != -1:
            content = content[idx:]

    clean_title = "Tutoriel"
    for line in content.splitlines():
        if line.startswith("title:"):
            raw_title = line.replace("title:", "", 1).strip()
            clean_title = raw_title.strip('"').strip("'")
            clean_title = clean_title.split(":", 1)[-1].split("-", 1)[-1].strip()
            break

    lines = content.splitlines()
    filtered_lines = []
    for line in lines:
        if any(line.startswith(k) for k in ["title:", "weight:", "prev_url:", "next_url:"]):
            continue
        filtered_lines.append(line)
    
    content_without_meta = "\n".join(filtered_lines)
    
    meta_lines = f'title: "{ep_num}. {clean_title}"\n'
    meta_lines += f'weight: {ep_num}\n'
    if prev_slug:
        meta_lines += f'prev_url: "{base_url_path}/{prev_slug}/"\n'
    if next_slug:
        meta_lines += f'next_url: "{base_url_path}/{next_slug}/"\n'
    
    if content_without_meta.startswith("---"):
        updated_content = content_without_meta.replace("---\n", f"---\n{meta_lines}", 1)
    else:
        updated_content = f"---\n{meta_lines}---\n{content_without_meta}"
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

def main():
    parser = argparse.ArgumentParser(description="Pipeline Batch Hugo - Traitement de dossiers complets")
    parser.add_argument("--dir", required=True, help="Dossier contenant toutes les vidéos à traiter")
    parser.add_argument("--engine", required=True, help="Moteur ou langage (ex: 'GDevelop 5')")
    parser.add_argument("--series", required=True, help="Nom de la série/dossier cible (ex: 'sweet-void')")
    parser.add_argument("--category", required=True, help="Catégorie Hugo (ex: 'Archive', 'Tutoriel')")
    args = parser.parse_args()
    
    source_dir = Path(args.dir)
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"❌ Dossier source introuvable ou invalide : {source_dir}")
        return

    # 1. Collecte et tri des vidéos par numéro d'épisode
    video_tasks = []
    print(f"🔍 Scan du dossier : {source_dir}")
    for file in source_dir.iterdir():
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            ep_num = extract_episode_number(file.name)
            if ep_num is not None:
                video_tasks.append((ep_num, file))
            else:
                print(f"⚠️ Ignoré (aucun numéro d'épisode détecté dans le nom) : {file.name}")

    if not video_tasks:
        print("❌ Aucune vidéo valide avec un numéro d'épisode n'a été trouvée.")
        return

    # Tri absolu par numéro d'épisode (1, 2, 3...) pour garantir la cohérence du maillage
    video_tasks.sort(key=lambda x: x[0])
    print(f"📦 {len(video_tasks)} vidéos prêtes à être traitées en série.")

    # 2. Chargement UNIQUE du modèle Whisper en mémoire pour toute la session
    print("🧠 Chargement du modèle Whisper (cette étape peut prendre une minute)...")
    whisper_model = whisper.load_model("base")

    # Configuration des chemins cibles
    engine_slug = re.sub(r'[^a-zA-Z0-9]', '-', args.engine.lower())
    engine_slug = re.sub(r'-+', '-', engine_slug).strip('-')
    target_dir = Path(BASE_CONTENT_DIR) / engine_slug / args.series
    base_url_path = f"/{engine_slug}/{args.series}"
    index_path = target_dir / INDEX_FILE_NAME

    # Assurer la structure de base
    target_dir.mkdir(parents=True, exist_ok=True)
    create_chapter_index_if_missing(target_dir, args.series, args.engine)
    series_index = load_index(index_path)

    # 3. Boucle de traitement principale
    for ep_num, video_path in video_tasks:
        print(f"\n🚀 --- TRAITEMENT ÉPISODE {ep_num} ({video_path.name}) ---")
        
        # Étape A : Transcription
        transcript = transcribe_video(video_path, whisper_model)
        
        # Étape B : Rédaction IA
        raw_article = generate_hugo_article(transcript, ep_num, args.engine, args.series, args.category)
        
        # Étape C : Extraction Slug (Méthode safe sans regex)
        current_slug = None
        clean_markdown = raw_article
        for line in raw_article.splitlines():
            if "SEO_SLUG:" in line:
                current_slug = line.split("SEO_SLUG:", 1)[-1].strip().strip('"').strip("'")
                clean_markdown = raw_article.replace(line, "").strip()
                break
                
        if not current_slug:
            current_slug = f"episode-{ep_num}"

        # Étape D : Enregistrement de l'épisode et mise à jour de l'index
        series_index[ep_num] = current_slug
        save_index(series_index, index_path)

        current_file_path = target_dir / f"{current_slug}.md"
        with open(current_file_path, "w", encoding="utf-8") as f:
            f.write(clean_markdown)

        # Étape E : Recalcul et rafraîchissement immédiat du maillage pour TOUTE la série traitée jusqu'ici
        print(f"🔗 Consolidation du maillage SEO et des poids (weight)...")
        for active_ep, slug in series_index.items():
            file_path = target_dir / f"{slug}.md"
            prev_slug = series_index.get(active_ep - 1, "index")
            next_slug = series_index.get(active_ep + 1, None)
            rewrite_front_matter_links(file_path, base_url_path, active_ep, prev_slug, next_slug)

    print(f"\n🎉 [BATCH TERMINÉ] Félicitations, les {len(video_tasks)} vidéos ont été traitées et rangées dans {target_dir} !")

if __name__ == "__main__":
    main()