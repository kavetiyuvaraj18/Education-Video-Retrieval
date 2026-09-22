from flask import Flask, render_template, request, jsonify
from flask import Flask, render_template, request
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)

@app.route("/", methods=["GET", "POST"])
def home():
    query = ""
    videos = []

    if request.method == "POST":
        query = request.form.get("query", "")

        response = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=20
        ).execute()

        for item in response.get("items", []):
            video = {
                "video_id": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
                "channel": item["snippet"]["channelTitle"],
                "published_at": item["snippet"]["publishedAt"]
            }

            videos.append(video)

    return render_template(
        "index.html",
        query=query,
        videos=videos
    )
@app.route("/api/search", methods=["POST"])
def api_search():
    data = request.get_json()
    query = data.get("query", "")

    response = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=20
    ).execute()

    videos = []

    for item in response.get("items", []):
        videos.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"]
        })

    return jsonify({
        "query": query,
        "videos": videos
    })
if __name__ == "__main__":
    app.run(debug=True)
