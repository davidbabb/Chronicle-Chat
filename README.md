# Historical Podcast (Python + OpenAI TTS)

Generate scripted, podcast-style interviews between a host and a historical figure.
Uses OpenAI for script generation + validation and OpenAI TTS for audio.

## Quick Start

1) **Python & FFmpeg**
   - Install Python 3.9+
   - Install FFmpeg (macOS: `brew install ffmpeg`, Ubuntu: `sudo apt install ffmpeg`, Windows: install from ffmpeg.org and add to PATH).

2) **Create a virtual environment (recommended)**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

3) **Install dependencies**
```bash
pip install -r requirements.txt
```

4) **Set your OpenAI API key**
   - Create a `.env` file at the project root with:
```
OPENAI_API_KEY=YOUR_KEY_HERE
```

5) **Run (example)**
```bash
python main.py abraham_lincoln
```

Output will be written to `output/episodes/<figure>_episode.mp3`.

## Notes

- We DO NOT clone real voices. We use generic, character-safe voices.
- The validator pass asks the LLM to suggest factual fixes before audio generation.
- `audio/intro_music.mp3` is optional. If present, it will be faded in/out automatically.
