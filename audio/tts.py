# THIS MODULE HANDLES TEXT-TO-SPEECH USING OPENAI TTS.  ALL COMMENTS IN CAPS.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def synthesize_line(text: str, voice: str, output_path: str) -> None:
    """
    # CONVERT A SINGLE LINE OF TEXT TO SPEECH AND WRITE TO DISK.
    # MODEL: GPT-4O-MINI-TTS (OR EQUIVALENT). ADJUST IF NEEDED.
    """
    # NOTE: THE PYTHON SDK EXPOSES AUDIO GENERATION VIA THE 'AUDIO.SPEECH.CREATE' METHOD ON SOME VERSIONS.
    # BELOW IS A COMPATIBLE CALLING PATTERN; UPDATE 'model' OR METHOD IF YOUR SDK DIFFERS.
    audio = _client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text,
        format="mp3",
    )
    with open(output_path, "wb") as f:
        f.write(audio.read())
