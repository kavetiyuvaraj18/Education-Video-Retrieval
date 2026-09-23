from ml.transcripts.youtube_transcript import get_transcript


video_id = "_uQrJ0TkZlc"

segments = get_transcript(video_id)

print("Total transcript segments:", len(segments))

if segments:
    print("First segment:")
    print(segments[0])

    print("\nLast segment:")
    print(segments[-1])

    print("\nTranscript end timestamp:",
          segments[-1]["end"])
else:
    print("No transcript found.")