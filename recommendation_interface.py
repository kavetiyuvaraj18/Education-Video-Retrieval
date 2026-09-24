from ml.retrieval.video_search import search_videos


def get_recommendations(query, videos, top_k=5):
    """
    Connect Member 1's Flask application
    with Member 2's ML recommendation system.

    Parameters:
        query: Student learning query.
        videos: Candidate YouTube video dictionaries.
        top_k: Number of recommendations.

    Returns:
        Ranked video dictionaries containing:
        video information, relevance score,
        timestamp, and relevant transcript.
    """

    if not query or not videos:
        return []

    # Extract YouTube video IDs
    video_ids = [
        video["video_id"]
        for video in videos
        if "video_id" in video
    ]

    if not video_ids:
        return []

    # Run Member 2 ML retrieval
    ml_results = search_videos(
        video_ids,
        query,
        top_k=top_k
    )

    # Match ML results with YouTube metadata
    video_lookup = {
        video["video_id"]: video
        for video in videos
    }

    recommendations = []

    for result in ml_results:

        video_id = result["video_id"]

        video = video_lookup.get(video_id)

        if not video:
            continue

        recommendation = video.copy()

        recommendation["score"] = result["score"]
        recommendation["start"] = result["start"]
        recommendation["end"] = result["end"]
        recommendation["relevant_text"] = result["text"]

        recommendations.append(recommendation)

    return recommendations[:top_k]