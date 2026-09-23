from ml.transcripts.youtube_transcript import get_transcript
from ml.preprocessing.timestamped_chunks import create_timestamped_chunks
from ml.embeddings.embedder import Embedder
from ml.vector_store.faiss_index import FAISSIndex
from ml.retrieval.recommender import Recommender


def build_video_index(video_ids):

    all_chunks = []
    valid_video_ids = []

    for video_id in video_ids:

        print(f"\nProcessing video: {video_id}")

        segments = get_transcript(video_id)

        if not segments:
            print("No transcript found.")
            continue

        chunks = create_timestamped_chunks(
            segments,
            chunk_size=3
        )

        for chunk in chunks:
            chunk["video_id"] = video_id

        all_chunks.extend(chunks)
        valid_video_ids.append(video_id)

    if not all_chunks:
        return None, None, None

    embedder = Embedder()

    texts = [
        chunk["text"]
        for chunk in all_chunks
    ]

    embeddings = embedder.encode(texts)

    dimension = embeddings.shape[1]

    faiss_index = FAISSIndex(dimension)
    faiss_index.add_embeddings(embeddings)

    recommender = Recommender(
        embedder,
        faiss_index
    )

    return recommender, all_chunks, valid_video_ids


def search_videos(recommender, chunks, query, top_k=5):

    results = recommender.recommend(
        query,
        chunks,
        top_k=top_k
    )

    return results


if __name__ == "__main__":

    video_ids = [
        "_uQrJ0TkZlc"
    ]

    query = "What is Python used for?"

    recommender, chunks, valid_video_ids = build_video_index(
        video_ids
    )

    if recommender is None:
        print("No videos could be processed.")
        exit()

    results = search_videos(
        recommender,
        chunks,
        query,
        top_k=5
    )

    print("\nStudent Query:")
    print(query)

    print("\nTop Results:")

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("Video ID:", result.get("video_id"))
        print("Score:", result["score"])
        print("Start:", result["start"])
        print("End:", result["end"])
        print("Text:", result["text"])