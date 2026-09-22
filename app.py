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


@app.route("/", methods=["GET", "POST"])
def home():

    query = ""
    videos = []
    error = None

    if request.method == "POST":

        query = request.form.get("query", "").strip()

        if query:

            try:

                videos = search_youtube_videos(query)

                videos = get_recommendations(
                    query,
                    videos
                )

            except Exception as e:

                print("YouTube API error:", e)

                error = (
                    "Unable to retrieve videos right now. "
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

        videos = search_youtube_videos(query)

        videos = get_recommendations(
            query,
            videos
        )

        return jsonify({
            "query": query,
            "videos": videos
        })

    except Exception as e:

        print("YouTube API error:", e)

        return jsonify({
            "error": "Unable to retrieve videos right now."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)