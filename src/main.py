import json

import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
yt_channel = os.getenv("YOUTUBE_CHANNEL_PLAYLIST")
videos_limit = int(os.getenv("LIMIT", "50"))
base_url = "https://www.googleapis.com/youtube/v3"

def get_playlist_videos():
    response = requests.get(f"{base_url}/playlistItems", params={
        "part": "snippet,contentDetails",
        "playlistId": yt_channel,
        "maxResults": videos_limit,
        "key": api_key,
    })
    data = response.json()

    video_items = []
    for item in data.get("items", []):
        video_id = item["contentDetails"]["videoId"]
        video_items.append(video_id)

    return video_items

def get_video_statistics(video_ids):
    if not video_ids:
        return []

    response = requests.get(f"{base_url}/videos", params={
        "part": "snippet,statistics,liveStreamingDetails",
        "id": ",".join(video_ids),
        "key": api_key,
    })
    data = response.json()

    videos = []
    for item in data.get("items", []):
        if "liveStreamingDetails" in item:
            continue

        snippet = item["snippet"]
        vid_id = item["id"]
        stats = item.get("statistics", {})

        thumbnails = snippet.get("thumbnails", {})
        thumbnail_url = (
            thumbnails.get("maxres", {}).get("url")
            or thumbnails.get("high", {}).get("url")
            or thumbnails.get("default", {}).get("url")
        )

        videos.append({
            "title": snippet.get("title"),
            "link": f"https://www.youtube.com/watch?v={vid_id}",
            "thumbnail": thumbnail_url,
            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)),
            "comments": int(stats.get("commentCount", 0)),
        })

    return videos

if __name__ == "__main__":
    try:
        print("Fetching video IDs...")
        video_ids = get_playlist_videos()

        print("Fetching video metadata...")
        videos = get_video_statistics(video_ids)

        with open("yt-data.json", "w",) as f:
            json.dump(videos, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"An error occurred: {e}")