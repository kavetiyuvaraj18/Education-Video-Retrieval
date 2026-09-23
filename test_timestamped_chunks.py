from ml.preprocessing.timestamped_chunks import create_timestamped_chunks


segments = [
    {"start": 0, "end": 5, "text": "Machine learning is useful."},
    {"start": 5, "end": 10, "text": "It learns patterns from data."},
    {"start": 10, "end": 15, "text": "It is used in many applications."},
    {"start": 15, "end": 20, "text": "Python is commonly used."}
]


chunks = create_timestamped_chunks(segments, chunk_size=2)


for chunk in chunks:
    print(chunk)