from ml.embeddings.embedder import Embedder
from ml.vector_store.faiss_index import FAISSIndex


chunks = [
    "Machine learning is a method of teaching computers to learn from data.",
    "Deep learning uses neural networks with multiple layers.",
    "Python is commonly used for machine learning applications."
]

embedder = Embedder()
embeddings = embedder.encode(chunks)

dimension = embeddings.shape[1]
faiss_index = FAISSIndex(dimension)

faiss_index.add_embeddings(embeddings)

query = "What is machine learning?"

query_embedding = embedder.encode([query])

scores, indices = faiss_index.search(
    query_embedding,
    top_k=2
)

print("\nQuery:", query)
print("\nTop matching chunks:")

for score, index in zip(scores[0], indices[0]):
    print(f"\nScore: {score:.4f}")
    print(chunks[index])