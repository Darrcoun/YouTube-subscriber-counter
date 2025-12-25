from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

def get_subscriber_count():
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    try:
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
