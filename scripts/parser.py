# THIS MODULE PARSES A SCRIPT WITH "HOST:" / "FIGURE:" LABELS INTO A LIST OF SEGMENTS.  ALL COMMENTS IN CAPS.
from typing import List, Dict

def parse_script(script_text: str) -> List[Dict[str, str]]:
    """
    # PARSE LABELED LINES INTO [{"speaker": "...", "text": "..."}].
    """
    segments = []
    current_speaker = None
    current_text = ""

    for raw in script_text.splitlines():
        line = raw.strip()
        if not line:
            continue

        # DETECT SPEAKER LABELS EXACTLY IN ALL CAPS FOLLOWED BY A COLON
        if line.endswith(":") and line[:-1].isupper():
            if current_speaker and current_text:
                segments.append({"speaker": current_speaker, "text": current_text.strip()})
            current_speaker = line[:-1]
            current_text = ""
        else:
            current_text += (" " if current_text else "") + line

    if current_speaker and current_text:
        segments.append({"speaker": current_speaker, "text": current_text.strip()})

    return segments
