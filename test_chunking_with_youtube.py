from ml.transcripts.youtube_transcript import get_transcript
from ml.preprocessing.timestamped_chunks import create_timestamped_chunks


video_id = "_uQrJ0TkZlc"

# Get YouTube transcript
segments = get_transcript(video_id)

print("Transcript segments:", len(segments))

# Create timestamped chunks
chunks = create_timestamped_chunks(
    segments,
    chunk_size=3
)

print("Timestamped chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0])

print("\nLast chunk:")
print(chunks[-1])