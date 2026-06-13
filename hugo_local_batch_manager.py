import os
import re
import json
import argparse
import time
import unicodedata
import urllib.request
import urllib.parse
from pathlib import Path
import whisper

# =====================================================================
# CONFIGURATION GÉNÉRALE LOCAL
# =====================================================================
OLLAMA_MODEL = "llama3:8b"  # Tu peux changer par "llama3" si tu préfères
OLLAMA_API_URL = "http://localhost:11434/api/generate"
BASE_CONTENT_DIR = "./content"
INDEX_FILE_NAME = ".series_index.json"
SUPPORTED_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".mp3", ".m4a"}
# =====================================================================

def extract_episode_number(filename):
    """Extrait le premier nombre trouvé dans le nom du fichier."""
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    return None

def sanitize_tag_line(line):
    """Nettoie en profondeur la ligne des tags pour Hugo."""
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
    """Transcrit la vidéo via Whisper en local."""
    print(f"\n🎬 [Whisper] Analyse et transcription : {video_path.name}...")
    result = whisper_model.transcribe(str(video_path), language="fr")
    return result["text"]

def generate_hugo_article_local(transcript, episode_num, engine, series_slug, category):
    """Demande au modèle local Ollama de générer l'article (Version stricte Français)."""
    print(f"🤖 [Ollama - {OLLAMA_MODEL}] Génération de l'article pour l'épisode {episode_num}...")
    
    system_instruction = (
        f"Tu es un rédacteur web expert en développement de jeux vidéo. Ton but est de transformer "
        f"une transcription brute de tutoriel en un article de blog rédigé STRICTEMENT EN FRANÇAIS.\n\n"
        "Consignes cruciales de langue et de format :\n"
        "- Rédige l'intégralité du texte en FRANÇAIS. Ne traduis JAMAIS en anglais.\n"
        "- Commence DIRECTEMENT le fichier par le Front Matter YAML entouré de '---'. Ne mets rien avant.\n"
        f"- Dans le Front Matter, inclus uniquement : title, date (2026-06-13), categories: ['{category}'], et tags.\n"
        "- Ne mets AUCUN champ 'prev_url', 'next_url' ou 'weight' dans le Front Matter.\n"
        "- JUSTE APRÈS le Front Matter (après le deuxième '---'), écris une introduction en français.\n"
        "- Ajoute ensuite le shortcode vidéo : {{< youtube-rgpd \"\" >}}.\n"
        "- Propose un résumé structuré en français avec des listes à puces des notions clés.\n"
        f"- Rédige une section '### Ce qui reste d'actualité aujourd'hui' en français liée à {engine}.\n"
        "- Termine le markdown avec le shortcode : {{< footer >}}.\n"
        "- TOUT À LA FIN du document, sur une ligne isolée, écris exactement : "
        "'SEO_SLUG: ton-titre-optimise-en-francais-sans-le-mot-episode'"
    )
    
    full_prompt = f"{system_instruction}\n\nVoici la transcription brute en français de l'épisode {episode_num} à traiter :\n\"\"\"\n{transcript}\n\"\"\""
    
    data = {
        "model": OLLAMA_MODEL,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.1  # Baisser la température à 0.1 rend le modèle beaucoup plus prévisible et obéissant
        }
    }
    
    req = urllib.request.Request(
        OLLAMA_API_URL, 
        data=json.dumps(data).encode("utf-8"), 
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["response"]
    except Exception as e:
        print(f"❌ Erreur lors de l'appel à Ollama : {e}")
        raise e

def create_chapter_index_if_missing(target_dir, series_name, engine_name):
    """Crée la page d'accueil de chapitre (_index.md)."""
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
    """Nettoie le fichier et injecte le titre, le weight, le maillage et assainit les tags."""
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
    parser = argparse.ArgumentParser(description="Pipeline Batch Hugo - 100% LOCAL avec Ollama")
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

    # Filtrage reprise de tâche
    tasks_to_process = []
    for ep_num, video_path in video_tasks:
        existing_slug = series_index.get(ep_num)
        if existing_slug and (target_dir / f"{existing_slug}.md").exists():
            print(f"⏭️  [Reprise] Épisode {ep_num} déjà fait. Passage au suivant.")
            continue
        tasks_to_process.append((ep_num, video_path))

    if not tasks_to_process:
        print("✅ Tous les épisodes ont déjà été générés !")
        return

    print(f"📦 {len(tasks_to_process)} vidéos à traiter localement.")

    # 2. Chargement unique de Whisper local
    print("🧠 Chargement du modèle Whisper...")
    whisper_model = whisper.load_model("base")

    # 3. Boucle de traitement principale
    for i, (ep_num, video_path) in enumerate(tasks_to_process):
        print(f"\n🚀 --- TRAITEMENT LOCAL ÉPISODE {ep_num} ({video_path.name}) ---")
        
        # Étape A : Transcription Whisper (Local)
        transcript = transcribe_video(video_path, whisper_model)
        
        # Étape B : Rédaction Ollama (Local - Plus de timeout, plus de quota !)
        raw_article = generate_hugo_article_local(transcript, ep_num, args.engine, args.series, args.category)
        
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

        # Étape E : Maillage global
        print(f"🔗 Consolidation du maillage SEO, des tags et des poids (weight)...")
        for active_ep, slug in series_index.items():
            file_path = target_dir / f"{slug}.md"
            prev_slug = series_index.get(active_ep - 1, "index")
            next_slug = series_index.get(active_ep + 1, None)
            rewrite_front_matter_links(file_path, base_url_path, active_ep, prev_slug, next_slug)

        print(f"💾 Épisode {ep_num} traité localement avec succès.")

        # PLUS DE TIME.SLEEP DE 60 SECONDES REQUIS ! On enchaîne !
        if i < len(tasks_to_process) - 1:
            time.sleep(1)

    print(f"\n🎉 [BATCH LOCAL TERMINÉ] Tout le dossier a été migré avec succès en 100% autonome !")

if __name__ == "__main__":
    main()