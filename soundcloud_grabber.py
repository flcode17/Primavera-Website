import requests

def get_recent_tracks(username, client_id, track_count=3):
    """
    Fetches the most recent tracks of a SoundCloud user.

    Args:
        username (str): The username of the SoundCloud user.
        client_id (str): Your SoundCloud API client ID.
        track_count (int): The number of most recent tracks to retrieve.

    Returns:
        list: A list of dictionaries containing track titles and URLs.
    """
    # Resolve the username to get the user ID
    resolve_url = f"https://api.soundcloud.com/resolve?url=https://soundcloud.com/{username}&client_id={client_id}"
    response = requests.get(resolve_url)

    if response.status_code != 200:
        print("Error resolving user profile:", response.json().get('errors', response.text))
        return []

    user_data = response.json()
    user_id = user_data['id']

    # Fetch the user's tracks
    tracks_url = f"https://api.soundcloud.com/users/{user_id}/tracks?client_id={client_id}"
    response = requests.get(tracks_url)

    if response.status_code != 200:
        print("Error fetching user tracks:", response.json().get('errors', response.text))
        return []

    tracks_data = response.json()

    # Sort and retrieve the most recent tracks
    recent_tracks = sorted(tracks_data, key=lambda x: x['created_at'], reverse=True)[:track_count]

    return [{"title": track["title"], "url": track["permalink_url"]} for track in recent_tracks]

# Replace with your SoundCloud API client ID
CLIENT_ID = "YOUR_SOUNDCLOUD_CLIENT_ID"

# Replace with the SoundCloud username
USERNAME = "DJ Pozitiff"

# Fetch the 3 most recent tracks
recent_tracks = get_recent_tracks(USERNAME, CLIENT_ID)

# Display the results
if recent_tracks:
    print("Most Recent Tracks:")
    for track in recent_tracks:
        print(f"Title: {track['title']}, URL: {track['url']}")
else:
    print("No tracks found.")
