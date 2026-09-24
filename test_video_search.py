from ml.retrieval.video_search import search_videos


video_ids = [
    "_uQrJ0TkZlc"
]

query = "What is Python used for?"


results = search_videos(
    video_ids,
    query,
    top_k=5
)


print("\nStudent Query:")
print(query)

print("\nTop Results:")

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("Video ID:", result["video_id"])
    print("Score:", result["score"])
    print("Start:", result["start"])
    print("End:", result["end"])
    print("Text:", result["text"])