from ml.transcripts.youtube_transcript import get_transcript
from ml.preprocessing.timestamped_chunks import create_timestamped_chunks
from ml.embeddings.embedder import Embedder
from ml.vector_store.faiss_index import FAISSIndex
from ml.retrieval.recommender import Recommender


# YouTube video
video_id = "_uQrJ0TkZlc"

# Student query
query = "What is Python used for?"


# 1. Get transcript
segments = get_transcript(video_id)

if not segments:
    print("No transcript found.")
    exit()

print("Transcript segments:", len(segments))


# 2. Create timestamped chunks
chunks = create_timestamped_chunks(
    segments,
    chunk_size=3
)

print("Timestamped chunks:", len(chunks))


# 3. Create embeddings
embedder = Embedder()

texts = [chunk["text"] for chunk in chunks]
embeddings = embedder.encode(texts)


# 4. Create FAISS index
dimension = embeddings.shape[1]

faiss_index = FAISSIndex(dimension)
faiss_index.add_embeddings(embeddings)


# 5. Create recommender
recommender = Recommender(
    embedder,
    faiss_index
)


# 6. Search using student query
results = recommender.recommend(
    query,
    chunks,
    top_k=5
)


# 7. Display results
print("\nStudent Query:")
print(query)

print("\nTop Results:")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Score:", result["score"])
    print("Start:", result["start"])
    print("End:", result["end"])
    print("Text:", result["text"])