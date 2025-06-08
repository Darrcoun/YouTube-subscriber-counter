from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)  # ✅ This must exist for Render + Gunicorn to work

YOUTUBE_API_KEY = os.environ.get("AIzaSyAuWVCegfLvuk4qwd0JJmWmIkrFybqtOy4")
CHANNEL_ID = os.environ.get("UCWiYh1ebBCW-hUBnjoSPceg")

def get_subscriber_count():
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}'
    response = requests.get(url)

    try:
        data = response.json()
        print("YouTube API response:", data)  # 👈 This will print to Render logs for debugging
        return int(data["items"][0]["statistics"]["subscriberCount"])
    except Exception as e:
        print("Error fetching subscriber count:", e)
        return 0

@app.route('/')
def home():
    return "YouTube Subscriber Counter is Running"

@app.route('/smiirl')
def smiirl_count():
    count = get_subscriber_count()
    return jsonify({"count": count})
