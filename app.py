def get_subscriber_count():
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={YOUTUBE_API_KEY}'
    response = requests.get(url)

    try:
        data = response.json()
        print("YouTube API response:", data)  # 👈 Debug print
        return int(data["items"][0]["statistics"]["subscriberCount"])
    except Exception as e:
        print("Error fetching subscriber count:", e)
        return 0
