from ml.transcripts.youtube_transcript import get_transcript
from ml.transcripts.whisper_transcript import WhisperTranscriber


def get_transcript_with_fallback(video_id, audio_file=None):
    """
    Get YouTube captions first.
    If captions are unavailable, use Whisper on the provided audio/video file.
    """

    transcript = get_transcript(video_id)

    if transcript:
        print("Using YouTube transcript.")
        return transcript

    if audio_file:
        print("YouTube transcript unavailable. Using Whisper.")
        transcriber = WhisperTranscriber("base")
        return transcriber.transcribe(audio_file)

    print("No transcript source available.")
    return []