from flask import Flask, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

app = Flask(__name__)

@app.route('/get-current-song', methods=['GET'])

def connect():
    scope="user-library-read user-top-read user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='1d5857199354488a9323cca294c9447a', client_secret='74ceeaab9d704b7984cc1c144fa0a926', redirect_uri='https://localhost:8888/callback', scope=scope))
    
    return sp
def getCurrent():
    return sp.current_playback()
sp = connect()

isSpotifyOn = True
try:
    sp.current_playback()
except Exception as e:
    isSpotifyOn = False
print(isSpotifyOn)
current_song = getCurrent()
songURL = current_song['item']["external_urls"]["spotify"]
def get_spotify_oembed(spotify_url):
    oembed_url = 'https://embed.spotify.com/oembed'
    params = {'url': spotify_url}

    response = requests.get(oembed_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Request failed with status code {response.status_code}')
        return None

spotify_url = songURL # replace with your Spotify URL
oembed_data = get_spotify_oembed(spotify_url)

#if oembed_data:
    #print(oembed_data["html"])
