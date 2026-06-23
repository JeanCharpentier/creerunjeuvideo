import os
import re
import json
import argparse
import time
import whisper
from pathlib import Path
from google import genai
from google.genai import types

GEMINI_MODEL = "gemini-3.1-flash-lite"
BASE_CONTENT_DIR = "./content"

def format_transcript_for_gemini(transcript):
    return "\n".join([transcript[i:i+800] for i in range(0, len(transcript), 800)])

def clean_yaml_value(value):
    clean = value.strip().strip("'\"").replace("'", "''")
    return f'"{clean}"'

def generate_engine_hub_page(target_dir, engine):
    """Génère la page d'accueil SEO du moteur si elle n'existe pas."""
    index_file = target_dir / "_index.md"
    if not index_file.exists():
        print(f"📄 [SEO] Création de la page hub pour {engine}...")
        client = genai.Client()
        prompt = f"Rédige une introduction SEO optimisée (h1 et texte) pour une catégorie de tutoriels sur le moteur de jeu {engine}."
        intro = client.models.generate_content(model=GEMINI_MODEL, contents=prompt).text
        content = ["---", f'title: "{engine.upper()} Tutorials"', '---', "", intro]
        index_file.write_text("\n".join(content), encoding="utf-8")

def generate_hugo_article_gemini(transcript, engine, category):
    client = genai.Client()
    system_instruction = (
        f"Tu es un expert GameDev. Rédige un article pour '{engine}'.\n"
        "1. Commence par Front Matter YAML (---).\n"
        "2. Titre : '[Titre]' (encadre le titre avec des guillemets doubles).\n"
        "3. Date (2026-06-17), categories: ['{category}'], tags.\n"
        "4. Après le Front Matter, une intro + {{< youtube-rgpd \"\" >}}.\n"
        "5. Résumé en listes, section '### Ce qui reste d'actualité aujourd'hui', {{< footer >}}.\n"
        "6. TOUT À LA FIN sur une ligne seule : SEO_SLUG: le-slug-de-l-article"
    )
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=f"Transcription de la vidéo :\n{transcript}",
        config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.3)
    )
    return response.text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True); parser.add_argument("--engine", required=True); parser.add_argument("--category", required=True)
    args = parser.parse_args()
    
    source_dir = Path(args.dir)
    target_dir = Path(BASE_CONTENT_DIR) / args.engine.lower().replace(" ", "-")
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. On assure l'existence du hub SEO
    generate_engine_hub_page(target_dir, args.engine)
    
    whisper_model = whisper.load_model("base")
    video_files = [f for f in source_dir.iterdir() if f.suffix.lower() in {".mp4", ".mkv", ".mov", ".avi"}]

    for video_path in video_files:
        print(f"\n🚀 Traitement : {video_path.name}")
        try:
            transcript = whisper_model.transcribe(str(video_path))["text"]
            raw_article = generate_hugo_article_gemini(format_transcript_for_gemini(transcript), args.engine, args.category)
            
            clean_lines, current_slug = [], video_path.stem.lower().replace(" ", "-")
            in_fm = False
            for line in raw_article.splitlines():
                if line.strip() == "---":
                    clean_lines.append(line); in_fm = not in_fm; continue
                if in_fm and ":" in line:
                    k, v = line.split(":", 1)
                    if k.strip() == "title": clean_lines.append(f'title: {clean_yaml_value(v)}')
                    elif k.strip() not in ["weight", "prev_url", "next_url"]: clean_lines.append(line)
                elif line.strip().lower().startswith("seo_slug:"): current_slug = re.sub(r'[^a-z0-9\-]', '', line.split(":", 1)[-1].strip().lower().replace(" ", "-"))
                else: clean_lines.append(line)
            
            (target_dir / f"{current_slug}.md").write_text("\n".join(clean_lines).strip(), encoding="utf-8")
        except Exception as e:
            print(f"❌ [ERREUR] {video_path.name} : {e}")
            continue 
        time.sleep(5)

if __name__ == "__main__":
    main()