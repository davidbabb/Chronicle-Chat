# THIS MODULE VALIDATES / CORRECTS THE SCRIPT FOR FACTUAL ACCURACY.  ALL COMMENTS IN CAPS.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_script(script_text: str) -> str:
    """
    # RUN A VALIDATION/CORRECTION PASS TO REDUCE FACTUAL ERRORS.
    # RETURNS: A POTENTIALLY CORRECTED SCRIPT TEXT.
    """
    prompt = f"""
    Review the following podcast script for historical accuracy.
    Identify any incorrect, misleading, or speculative statements.
    Provide a corrected version of the entire script with suggested fixes applied,
    preserving the original structure, speaker labels, and style.

    Script:
    {script_text}
    """

    resp = _client.chat.completions.create(
        model="gpt-5.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return resp.choices[0].message.content
