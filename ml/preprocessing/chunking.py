def create_chunks(transcript, chunk_size=3):
    """
    Split a transcript into small groups of sentences.
    """

    if not transcript:
        return []

    sentences = [
        sentence.strip()
        for sentence in transcript.split(".")
        if sentence.strip()
    ]

    chunks = []

    for i in range(0, len(sentences), chunk_size):
        chunk = ". ".join(sentences[i:i + chunk_size])
        chunks.append(chunk + ".")

    return chunks