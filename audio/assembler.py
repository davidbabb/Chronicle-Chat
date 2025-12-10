# THIS MODULE STITCHES MP3 SEGMENTS INTO A SINGLE EPISODE.  ALL COMMENTS IN CAPS.
import os
from typing import List, Optional
from pydub import AudioSegment

def assemble_episode(segment_files: List[str], output_path: str, intro_music: Optional[str] = None) -> None:
    """
    # COMBINE SEGMENTS (MP3) WITH OPTIONAL INTRO MUSIC AND SILENT GAPS.
    """
    final = AudioSegment.silent(duration=1000)  # 1-SECOND LEAD-IN

    # OPTIONAL INTRO MUSIC (WITH GAIN AND FADES)
    if intro_music and os.path.exists(intro_music):
        try:
            music = AudioSegment.from_file(intro_music)
            music = music.apply_gain(-6).fade_in(1500).fade_out(1500)
            final += music
        except Exception:
            # FAIL-SAFE: SKIP MUSIC IF DECODING FAILS
            pass

    # APPEND EACH SPOKEN SEGMENT WITH A SHORT PAUSE
    for f in segment_files:
        try:
            seg = AudioSegment.from_file(f)
            final += seg
            final += AudioSegment.silent(duration=500)  # 0.5-SECOND PAUSE
        except Exception:
            # SKIP CORRUPT OR MISSING FILES
            continue

    # GLOBAL FADES
    final = final.fade_in(1200).fade_out(1800)

    # ENSURE OUTPUT DIR EXISTS
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final.export(output_path, format="mp3")
