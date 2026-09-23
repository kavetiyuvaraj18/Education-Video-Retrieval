from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    """
    Fetch the available YouTube transcript for a video.
    """

    api = YouTubeTranscriptApi()

    try:
        transcript = api.fetch(video_id)

        segments = []

        for item in transcript:
            segments.append({
                "start": item.start,
                "end": item.start + item.duration,
                "text": item.text
            })

        return segments

    except Exception as error:
        print(f"Transcript could not be retrieved: {error}")
        return []