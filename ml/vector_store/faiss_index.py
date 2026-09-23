import faiss
import numpy as np


class FAISSIndex:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)

    def add_embeddings(self, embeddings):
        """
        Add normalized embedding vectors to the FAISS index.
        """
        embeddings = np.asarray(embeddings, dtype="float32")
        self.index.add(embeddings)

    def search(self, query_embedding, top_k=5):
        """
        Search for the most similar transcript chunks.
        """
        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        scores, indices = self.index.search(query_embedding, top_k)

        return scores, indices