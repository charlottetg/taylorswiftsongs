import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

SPOTIFY_ID = '78c4c1fc79184a1d88c9b737eb10c00a'
SPOTIFY_SECRET = '324b59e085114c728947f7a4ab2f2481'
redirect_uri = 'http://google.com/callback/'


def prepare_spotify_query(song):
    song_name = song['Title']
    album_name = song['Album']
    if album_name == 'Red' or album_name == 'Fearless':
        song_name = song_name + ' (Taylor\'s Version)'
        album_name = album_name + ' (Taylor\'s Version)'
    query_base = f"%20track:{song_name.replace(' ', '%20')}%20artist:Taylor%20Swift%20"
    try:
        song_feature = song['ft']
        if song["Album"] == 'none':
            return f"{query_base}{song_feature.replace(' ', '%20')}"
        else:
            return f"{query_base}{song_feature.replace(' ', '%20')}%20album:{album_name.replace(' ', '%20')}"
    except:
        return f"{query_base}album:{album_name.replace(' ', '%20')}"


def open_song(song='', query=''):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_ID,
                                                               client_secret=SPOTIFY_SECRET))
    if query == '':
        query = prepare_spotify_query(song)
    results = sp.search(query, 1, 0, "track")
    try:
        webbrowser.open(results['tracks']['items'][0]['external_urls']['spotify'], new=0)
        return 'Opened in new tab'
    except:
        return f'No results for {query}'