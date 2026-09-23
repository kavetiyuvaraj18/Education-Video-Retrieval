class Recommender:
    def __init__(self, embedder, faiss_index):
        self.embedder = embedder
        self.faiss_index = faiss_index

    def recommend(self, query, top_k=5):
        """
        Retrieve the most relevant transcript chunks for a query.
        """

        query_embedding = self.embedder.encode([query])

        scores, indices = self.faiss_index.search(
            query_embedding,
            top_k
        )

        return scores, indices