class Recommender:
    def __init__(self, embedder, faiss_index):
        self.embedder = embedder
        self.faiss_index = faiss_index

    def recommend(self, query, chunks, top_k=5):
        """
        Retrieve the most relevant timestamped transcript chunks.
        """

        query_embedding = self.embedder.encode([query])

        scores, indices = self.faiss_index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index < len(chunks):
                results.append({
                    "video_id": chunks[index]["video_id"],
                    "score": float(score),
                    "start": chunks[index]["start"],
                    "end": chunks[index]["end"],
                    "text": chunks[index]["text"]
                })

        return results