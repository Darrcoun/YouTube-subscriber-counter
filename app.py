from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

YOUTUBE_API_KEY = "YOUR_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"

def get_subscriber_count():
    """Fetch the latest subscriber count from YouTube API."""
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return int(data["items"][0]["statistics"]["subscriberCount"])

@app.route('/smiirl', methods=['GET'])
def smiirl_count():
    """Return subscriber count in JSON format for Smiirl."""
    count = get_subscriber_count()
    return jsonify({"value": count})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get the port from environment variable, default to 5000
    app.run(host='0.0.0.0', port=port)
