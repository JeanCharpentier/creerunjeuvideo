import os
import re
import json
import argparse
import time
import whisper
from pathlib import Path
from google import genai
from google.genai import types

# =====================================================================
# CONFIGURATION
# =====================================================================
GEMINI_MODEL = "gemini-3.1-flash-lite"
BASE_CONTENT_DIR = "./content"

def format_transcript_for_gemini(transcript):
    """Découpe le texte par blocs pour éviter de saturer l'IA."""
    return "\n".join([transcript[i:i+800] for i in range(0, len(transcript), 800)])

def clean_yaml_value(value):
    """Nettoie une valeur YAML : échappe les apostrophes et entoure de doubles guillemets."""
    # Enlève les guillemets existants, double les apostrophes, remet des guillemets doubles
    clean = value.strip().strip("'\"").replace("'", "''")
    return f'"{clean}"'

def save_transcript(transcript, video_path):
    """Sauvegarde le texte brut en .txt à côté de la vidéo."""
    txt_path = video_path.with_suffix(".txt")
    txt_path.write_text(transcript, encoding="utf-8")

def generate_hugo_article_gemini(transcript, episode_num, engine, category):
    """Envoie la transcription à Gemini avec les instructions de formatage."""
    client = genai.Client()
    system_instruction = (
        f"Tu es un expert GameDev. Rédige un article pour '{engine}'.\n"
        "1. Commence par Front Matter YAML (---).\n"
        f"2. Titre : '{episode_num}. [Titre]' (encadre le titre avec des guillemets doubles).\n"
        "3. Date (2026-06-17), categories: ['{category}'], tags.\n"
        "4. Après le Front Matter, une intro + {{< youtube-rgpd \"\" >}}.\n"
        "5. Résumé en listes, section '### Ce qui reste d'actualité aujourd'hui', {{< footer >}}.\n"
        "6. TOUT À LA FIN sur une ligne seule : SEO_SLUG: le-slug-de-l-article"
    )
    
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=f"Transcription épisode {episode_num}:\n{transcript}",
        config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.3)
    )
    return response.text

def generate_series_index_page(target_dir, series_index, engine):
    """Génère le _index.md de la série avec une intro générée par l'IA."""
    print("📄 [Index] Génération de la page sommaire...")
    client = genai.Client()
    prompt = f"Rédige une courte introduction (3-4 phrases) pour un index de série Hugo sur le moteur {engine}."
    response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
    intro = response.text if response.text else "Bienvenue dans cette série de tutoriels."

    content = ["---", 'title: "Sommaire de la série"', 'weight: 0', "---", "", intro, "", "# Liste des épisodes", ""]
    for ep_num in sorted(series_index.keys(), key=int):
        content.append(f"- [Épisode {ep_num}](./{series_index[ep_num]}/)")
    (target_dir / "_index.md").write_text("\n".join(content), encoding="utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True); parser.add_argument("--engine", required=True)
    parser.add_argument("--series", required=True); parser.add_argument("--category", required=True)
    args = parser.parse_args()
    
    source_dir = Path(args.dir)
    target_dir = Path(BASE_CONTENT_DIR) / args.engine.lower().replace(" ", "-") / args.series
    target_dir.mkdir(parents=True, exist_ok=True)
    
    index_path = target_dir / ".series_index.json"
    series_index = json.loads(index_path.read_text()) if index_path.exists() else {}
    whisper_model = whisper.load_model("base")
    
    video_tasks = sorted([(int(re.search(r'\d+', f.name).group()), f) for f in source_dir.iterdir() if f.suffix.lower() in {".mp4", ".mkv", ".mov", ".avi"}], key=lambda x: x[0])

    for ep_num, video_path in video_tasks:
        if str(ep_num) in series_index and (target_dir / f"{series_index[str(ep_num)]}.md").exists():
            continue
            
        print(f"\n🚀 Traitement Épisode {ep_num}...")
        try:
            # 1. Transcription et sauvegarde backup
            transcript = whisper_model.transcribe(str(video_path))["text"]
            save_transcript(transcript, video_path)
            
            # 2. Génération article via Gemini
            raw_article = generate_hugo_article_gemini(format_transcript_for_gemini(transcript), ep_num, args.engine, args.category)
            if not raw_article: raise ValueError("Réponse IA vide")

            # 3. Nettoyage YAML et extraction Slug
            clean_lines, current_slug = [], f"episode-{ep_num}"
            in_fm = False
            for line in raw_article.splitlines():
                if line.strip() == "---":
                    clean_lines.append(line); in_fm = not in_fm; continue
                
                if in_fm and ":" in line:
                    k, v = line.split(":", 1)
                    if k.strip() == "title": 
                        clean_lines.append(f'title: {clean_yaml_value(v)}')
                        clean_lines.append(f'weight: {ep_num}')
                    elif k.strip() not in ["weight", "prev_url", "next_url"]: 
                        clean_lines.append(line)
                elif line.strip().lower().startswith("seo_slug:"): 
                    current_slug = re.sub(r'[^a-z0-9\-]', '', line.split(":", 1)[-1].strip().lower().replace(" ", "-"))
                else: 
                    clean_lines.append(line)
            
            # 4. Enregistrement
            series_index[str(ep_num)] = current_slug
            (target_dir / f"{current_slug}.md").write_text("\n".join(clean_lines).strip(), encoding="utf-8")
            print(f"✅ Succès : {current_slug}.md (poids: {ep_num})")
            
        except Exception as e:
            print(f"❌ [ERREUR] Échec sur l'épisode {ep_num} : {e}")
            continue 
        time.sleep(5)
        
    generate_series_index_page(target_dir, series_index, args.engine)
    index_path.write_text(json.dumps(series_index, indent=4), encoding="utf-8")
    print("\n🎉 Batch terminé !")

if __name__ == "__main__":
    main()