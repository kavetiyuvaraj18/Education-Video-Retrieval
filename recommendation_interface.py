def get_recommendations(query, videos):
    """
    Recommendation interface.

    Member 1 sends:
        query
        candidate videos

    Member 2 will later replace this placeholder
    with the actual recommendation system.
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

            # These will be produced by Member 2.
            "relevance_score": None,
            "timestamp": None
        }

        recommendations.append(recommendation)

    return recommendations