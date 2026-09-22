def get_recommendations(query, videos, top_k=5):
    """
    Recommendation interface.

    Parameters:
        query:
            Student's learning query.

        videos:
            Candidate videos retrieved from YouTube.

        top_k:
            Number of final recommended videos.

    Returns:
        Top-K recommended videos.
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

            # These values will later come from
            # Member 2's recommendation model.
            "relevance_score": None,
            "timestamp": None
        }

        recommendations.append(recommendation)

    # Temporary behavior:
    # Until Member 2's model is connected,
    # return the first top_k candidates.
    return recommendations[:top_k]