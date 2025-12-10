# THIS MODULE GENERATES A PODCAST SCRIPT USING OPENAI.  ALL COMMENTS IN CAPS PER USER PREFERENCE.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# CREATE A SINGLETON CLIENT
_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(figure_name: str, figure_description: str, duration: str = "10 minutes") -> str:
    """
    # GENERATE A DRAFT PODCAST SCRIPT.
    # RETURNS: RAW SCRIPT TEXT WITH SPEAKER LABELS ("HOST:" / "FIGURE:").
    """
    prompt = f"""
    Create a podcast interview between a host named Alex and the historical figure {figure_name}.
    Description for context: {figure_description}

    Target length: {duration}
    Requirements:
    - Conversational, modern tone suitable for education.
    - Accurate historical facts only.
    - Use labeled blocks EXACTLY like:
      HOST:
      FIGURE:
    - Do NOT imitate any real recorded voice; use a dramatized interpretation only.
    - Keep each block under 2–3 sentences.
    - Include 8–12 Q&A sequences.
    - Begin with a short host introduction.
    - End with a short outro by the host.
    """

    # CALL THE CHAT COMPLETIONS ENDPOINT
    resp = _client.chat.completions.create(
        model="gpt-5.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return resp.choices[0].message.content
