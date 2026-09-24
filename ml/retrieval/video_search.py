from ml.transcripts.youtube_transcript import get_transcript
from ml.preprocessing.timestamped_chunks import create_timestamped_chunks
from ml.embeddings.embedder import Embedder
from ml.vector_store.faiss_index import FAISSIndex
from ml.retrieval.recommender import Recommender


def search_videos(video_ids, query, top_k=5):

    all_chunks = []

    # Get transcripts and create timestamped chunks
    for video_id in video_ids:

        segments = get_transcript(video_id)

        if not segments:
            continue

        chunks = create_timestamped_chunks(
            segments,
            chunk_size=3
        )

        for chunk in chunks:
            chunk["video_id"] = video_id

        all_chunks.extend(chunks)

    if not all_chunks:
        return []

    # Create embeddings
    embedder = Embedder()

    texts = [
        chunk["text"]
        for chunk in all_chunks
    ]

    embeddings = embedder.encode(texts)

    # Create FAISS index
    dimension = embeddings.shape[1]

    faiss_index = FAISSIndex(dimension)
    faiss_index.add_embeddings(embeddings)

    # Search
    recommender = Recommender(
        embedder,
        faiss_index
    )

    results = recommender.recommend(
        query,
        all_chunks,
        top_k=top_k
    )

    return results