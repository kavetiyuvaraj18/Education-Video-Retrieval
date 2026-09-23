def create_timestamped_chunks(transcript_segments, chunk_size=3):
    """
    Group timestamped transcript segments into chunks.
    """

    if not transcript_segments:
        return []

    chunks = []

    for i in range(0, len(transcript_segments), chunk_size):
        group = transcript_segments[i:i + chunk_size]

        chunk = {
            "start": group[0]["start"],
            "end": group[-1]["end"],
            "text": " ".join(
                segment["text"] for segment in group
            )
        }

        chunks.append(chunk)

    return chunks