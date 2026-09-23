def process_transcript(transcript):
    """
    Clean a transcript before further processing.
    """
    if not transcript:
        return ""

    transcript = transcript.strip()
    return transcript