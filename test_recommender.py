from ml.embeddings.embedder import Embedder
from ml.vector_store.faiss_index import FAISSIndex
from ml.retrieval.recommender import Recommender


chunks = [
    {
        "start": 0,
        "end": 10,
        "text": "Machine learning allows computers to learn from data."
    },
    {
        "start": 10,
        "end": 20,
        "text": "Deep learning uses neural networks with multiple layers."
    },
    {
        "start": 20,
        "end": 30,
        "text": "Python is commonly used for machine learning applications."
    }
]


embedder = Embedder()

texts = [chunk["text"] for chunk in chunks]
embeddings = embedder.encode(texts)

dimension = embeddings.shape[1]
faiss_index = FAISSIndex(dimension)
faiss_index.add_embeddings(embeddings)

recommender = Recommender(embedder, faiss_index)

results = recommender.recommend(
    "What is machine learning?",
    chunks,
    top_k=2
)

print("\nRecommendations:")

for result in results:
    print("\nScore:", result["score"])
    print("Start:", result["start"])
    print("End:", result["end"])
    print("Text:", result["text"])