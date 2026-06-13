import os
import re
import json
import argparse
import time
import unicodedata
from pathlib import Path
import whisper
from google import genai
from google.genai import types
from google.genai.errors import ClientError  # Import pour intercepter la 429

# =====================================================================
# CONFIGURATION GÉNÉRALE
# =====================================================================
GEMINI_MODEL = "gemini-3.1-flash-lite" 
BASE_CONTENT_DIR = "./content"  # Racine de ton dossier de contenu Hugo
INDEX_FILE_NAME = ".series_index.json"
SUPPORTED_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".mp3", ".m4a"}
# =====================================================================

def extract_episode_number(filename):
    """Extrait le premier nombre trouvé dans le nom du fichier pour déterminer l'épisode."""
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    return None

def sanitize_tag_line(line):
    """Nettoie en profondeur la ligne des tags pour Hugo (retrait accents, apostrophes)."""
    if not line.startswith("tags:"):
        return line
    prefix, tags_part = line.split("tags:", 1)
    tags_part = tags_part.replace("\\'", "'").replace('\\"', '"')
    tags_part = tags_part.replace("'", " ").replace('"', " ")
    tags_part = "".join(
        c for c in unicodedata.normalize('NFKD', tags_part)
        if not unicodedata.combining(c)
    )
    raw_tags = [t.strip() for t in tags_part.replace("[", "").replace("]", "").split(",") if t.strip()]
    clean_tags_list = [f"'{t}'" for t in raw_tags]
    return f"tags: [{', '.join(clean_tags_list)}]"

def transcribe_video(video_path, whisper_model):
    """Transcrit la vidéo directement via l'instance Whisper partagée."""
    print(f"\n🎬 [Whisper] Analyse et transcription : {video_path.name}...")
    result = whisper_model.transcribe(str(video_path), language="fr")
    return result["text"]

def generate_hugo_article(transcript, episode_num, engine, series_slug, category):
    """Demande à l'IA de générer l'article brut avec gestion résiliente des quotas (429)."""
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
    
    # Boucle infinie de tentative de requête pour absorber le "Resource Exhausted"
    while True:
        try:
            print(f"✍️  [Gemini] Requête API pour l'épisode {episode_num}...")
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.3
                )
            )
            return response.text
        except ClientError as e:
            if e.code == 429:
                print("\n🛑 [QUOTA EXCÉDÉ] Gemini signale une surcharge ou fin de quota journalier.")
                print("⏳ Le script se met en sommeil pendant 65 secondes avant de retenter l'envoi...")
                time.sleep(65)
            else:
                # Si c'est une autre erreur client (400, 403, etc.), on la lève pour ne pas boucler à l'infini
                raise e

def create_chapter_index_if_missing(target_dir, series_name, engine_name):
    """Crée la page d'accueil de chapitre (_index.md) propre à l'architecture Hugo."""
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
"""
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(chapter_content)

def load_index(index_path):
    """Charge l'index local de la série."""
    if index_path.exists():
        with open(index_path, "r", encoding="utf-8") as f:
            try:
                return {int(k): v for k, v in json.load(f).items()}
            except json.JSONDecodeError:
                return {}
    return {}

def save_index(index, index_path):
    """Sauvegarde l'index de la série."""
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=4)

def rewrite_front_matter_links(file_path, base_url_path, ep_num, prev_slug, next_slug):
    """Nettoie le fichier et injecte le titre formaté, le weight, le maillage et assainit les tags."""
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
            while True:
                parts = clean_title.split(".", 1)
                if len(parts) > 1 and parts[0].strip().isdigit():
                    clean_title = parts[1].strip()
                else:
                    break
            clean_title = clean_title.split(":", 1)[-1].split("-", 1)[-1].strip()
            break

    lines = content.splitlines()
    filtered_lines = []
    for line in lines:
        if line.startswith("tags:"):
            line = sanitize_tag_line(line)
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
    parser = argparse.ArgumentParser(description="Pipeline Batch Hugo - Résilience Quotas & Reprise de tâche")
    parser.add_argument("--dir", required=True, help="Dossier contenant toutes les vidéos à traiter")
    parser.add_argument("--engine", required=True, help="Moteur ou langage (ex: 'GDevelop 5')")
    parser.add_argument("--series", required=True, help="Nom de la série/dossier cible (ex: 'sweet-void')")
    parser.add_argument("--category", required=True, help="Catégorie Hugo (ex: 'Archive', 'Tutoriel')")
    args = parser.parse_args()
    
    source_dir = Path(args.dir)
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"❌ Dossier source introuvable ou invalide : {source_dir}")
        return

    # 1. Collecte et tri des vidéos
    video_tasks = []
    for file in source_dir.iterdir():
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
            ep_num = extract_episode_number(file.name)
            if ep_num is not None:
                video_tasks.append((ep_num, file))

    if not video_tasks:
        print("❌ Aucune vidéo valide trouvée.")
        return

    video_tasks.sort(key=lambda x: x[0])

    # Configuration des chemins cibles
    engine_slug = re.sub(r'[^a-zA-Z0-9]', '-', args.engine.lower()).strip('-')
    target_dir = Path(BASE_CONTENT_DIR) / engine_slug / args.series
    base_url_path = f"/{engine_slug}/{args.series}"
    index_path = target_dir / INDEX_FILE_NAME

    target_dir.mkdir(parents=True, exist_ok=True)
    create_chapter_index_if_missing(target_dir, args.series, args.engine)
    series_index = load_index(index_path)

    # FILTRAGE : On retire les épisodes qui possèdent déjà un fichier markdown valide dans le dossier
    tasks_to_process = []
    for ep_num, video_path in video_tasks:
        existing_slug = series_index.get(ep_num)
        if existing_slug and (target_dir / f"{existing_slug}.md").exists():
            print(f"⏭️  [Reprise] Épisode {ep_num} déjà traité ({existing_slug}.md). Passage au suivant.")
            continue
        tasks_to_process.append((ep_num, video_path))

    if not tasks_to_process:
        print("✅ Tous les épisodes de ce dossier ont déjà été générés !")
        return

    print(f"📦 {len(tasks_to_process)} vidéos restent à traiter sur les {len(video_tasks)} initiales.")

    # 2. Chargement unique de Whisper
    print("🧠 Chargement du modèle Whisper...")
    whisper_model = whisper.load_model("base")

    # 3. Boucle de traitement principale
    for i, (ep_num, video_path) in enumerate(tasks_to_process):
        print(f"\n🚀 --- TRAITEMENT ÉPISODE {ep_num} ({video_path.name}) ---")
        
        # Étape A : Transcription
        transcript = transcribe_video(video_path, whisper_model)
        
        # Étape B : Rédaction IA (Gère les erreurs 429 de manière transparente)
        raw_article = generate_hugo_article(transcript, ep_num, args.engine, args.series, args.category)
        
        # Étape C : Extraction Slug
        current_slug = None
        clean_markdown = raw_article
        for line in raw_article.splitlines():
            if "SEO_SLUG:" in line:
                current_slug = line.split("SEO_SLUG:", 1)[-1].strip().strip('"').strip("'")
                clean_markdown = raw_article.replace(line, "").strip()
                break
        if not current_slug:
            current_slug = f"episode-{ep_num}"

        # Étape D : Enregistrement
        series_index[ep_num] = current_slug
        save_index(series_index, index_path)

        current_file_path = target_dir / f"{current_slug}.md"
        with open(current_file_path, "w", encoding="utf-8") as f:
            f.write(clean_markdown)

        # Étape E : Rafraîchissement global du maillage
        print(f"🔗 Consolidation du maillage SEO, des tags et des poids (weight)...")
        for active_ep, slug in series_index.items():
            file_path = target_dir / f"{slug}.md"
            prev_slug = series_index.get(active_ep - 1, "index")
            next_slug = series_index.get(active_ep + 1, None)
            rewrite_front_matter_links(file_path, base_url_path, active_ep, prev_slug, next_slug)

        print(f"💾 Épisode {ep_num} traité et sauvegardé avec succès.")

        # Pause standard de sécurité pour lisser le flux si d'autres vidéos arrivent
        if i < len(tasks_to_process) - 1:
            print("⏳ Pause de sécurité de 10 secondes entre les traitements...")
            time.sleep(10)

    print(f"\n🎉 [BATCH TERMINÉ] Traitement fini avec succès.")

if __name__ == "__main__":
    main()