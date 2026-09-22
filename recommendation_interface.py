def get_recommendations(query, videos, top_k=5):
    """
    Interface between Member 1 and Member 2's
    recommendation system.

    Parameters:
        query:
            Student's learning query.

        videos:
            Candidate videos retrieved from YouTube.

        top_k:
            Number of final recommended videos.

    Returns:
        List of recommended videos.

    Member 2 will later replace the temporary
    recommendation logic with the actual:

        Sentence Transformer
        -> Embeddings
        -> FAISS
        -> Cosine Similarity
        -> Ranking
        -> Timestamp Retrieval
    """

    recommendations = []

    for video in videos:

        recommendation = {
            "video_id": video["video_id"],
            "title": video["title"],
            "description": video["description"],
            "thumbnail": video["thumbnail"],
            "channel": video["channel"],
            "published_at": video["published_at"],

            # Member 2 will provide the actual value.
            "relevance_score": None,

            # Member 2 will provide the actual
            # relevant timestamp in seconds.
            "timestamp": None
        }

        recommendations.append(recommendation)

    # Temporary behavior until Member 2's
    # recommendation model is integrated.
    return recommendations[:top_k]