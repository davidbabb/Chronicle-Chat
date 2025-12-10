# MAIN PIPELINE: GENERATE → VALIDATE → PARSE → TTS → ASSEMBLE.  ALL COMMENTS IN CAPS.
import sys
import os
import json
from scripts.script_generator import generate_script
from scripts.script_validator import validate_script
from scripts.parser import parse_script
from audio.tts import synthesize_line
from audio.assembler import assemble_episode

FIGURES_PATH = os.path.join("config", "figures.json")
VOICES_PATH = os.path.join("config", "voices.json")

def load_config():
    # LOAD FIGURES AND VOICE MAPS
    with open(FIGURES_PATH, "r", encoding="utf-8") as f:
        figures = json.load(f)
    with open(VOICES_PATH, "r", encoding="utf-8") as f:
        voices = json.load(f)
    return figures, voices

def main(figure_key: str, duration: str = "10 minutes"):
    figures, voices = load_config()
    if figure_key not in figures:
        raise SystemExit(f"Unknown figure key: {figure_key}. Edit config/figures.json to add it.")

    figure = figures[figure_key]
    os.makedirs(os.path.join("output", "segments"), exist_ok=True)
    os.makedirs(os.path.join("output", "episodes"), exist_ok=True)

    print("Generating script...")
    raw_script = generate_script(figure["name"], figure["description"], duration=duration)

    print("Validating script...")
    clean_script = validate_script(raw_script)

    print("Parsing script...")
    segments = parse_script(clean_script)

    segment_files = []
    print("Generating TTS segments...")
    for i, seg in enumerate(segments):
        speaker = seg.get("speaker", "").strip()
        text = seg.get("text", "").strip()
        if not text:
            continue

        # SELECT VOICE: HOST VS FIGURE
        voice = voices["host"] if speaker == "HOST" else voices["generic_historical"]

        out_path = os.path.join("output", "segments", f"seg_{i:03d}.mp3")
        synthesize_line(text, voice, out_path)
        segment_files.append(out_path)

    print("Assembling episode...")
    out_episode = os.path.join("output", "episodes", f"{figure_key}_episode.mp3")
    assemble_episode(segment_files, out_episode, intro_music=os.path.join("audio", "intro_music.mp3"))

    print(f"Episode complete → {out_episode}")

if __name__ == "__main__":
    # USAGE: python main.py abraham_lincoln [optional_duration]
    figure = sys.argv[1] if len(sys.argv) > 1 else "abraham_lincoln"
    duration = sys.argv[2] if len(sys.argv) > 2 else "10 minutes"
    main(figure, duration)
