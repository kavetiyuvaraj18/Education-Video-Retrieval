from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
from dotenv import load_dotenv
from recommendation_interface import get_recommendations
import os

load_dotenv()

app = Flask(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise RuntimeError(
        "YOUTUBE_API_KEY is missing. Check your .env file."
    )

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def search_youtube_videos(query):

    response = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        order="relevance",
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

    return videos


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "running",
        "youtube_api": "configured",
        "recommendation_interface": "connected"
    })


@app.route("/", methods=["GET", "POST"])
def home():

    query = ""
    videos = []
    error = None

    if request.method == "POST":

        query = request.form.get("query", "").strip()

        if query:

            try:

                candidate_videos = search_youtube_videos(query)

                videos = get_recommendations(
                    query,
                    candidate_videos,
                    top_k=5
                )

            except Exception as e:

                print("Application error:", e)

                error = (
                    "Unable to retrieve recommendations right now. "
                    "Please try again."
                )

    return render_template(
        "index.html",
        query=query,
        videos=videos,
        error=error
    )


@app.route("/api/search", methods=["POST"])
def api_search():

    data = request.get_json()

    if not data:

        return jsonify({
            "error": "Request body is required"
        }), 400

    query = data.get("query", "").strip()

    if not query:

        return jsonify({
            "error": "Search query is required"
        }), 400

    try:

        candidate_videos = search_youtube_videos(query)

        videos = get_recommendations(
            query,
            candidate_videos,
            top_k=5
        )

        return jsonify({
            "query": query,
            "candidate_count": len(candidate_videos),
            "recommendation_count": len(videos),
            "videos": videos
        })

    except Exception as e:

        print("Application error:", e)

        return jsonify({
            "error": "Unable to retrieve recommendations right now."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)