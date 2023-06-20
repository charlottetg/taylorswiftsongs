import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

SPOTIFY_ID = '78c4c1fc79184a1d88c9b737eb10c00a'
SPOTIFY_SECRET = '324b59e085114c728947f7a4ab2f2481'
redirect_uri = 'http://google.com/callback/'

albumids = {'TS': '7mzrIsaAjnXihW3InKjlC3',
            'Fearless': '4hDok0OAJd57SGIT8xuWJH',
            'Speak Now': '5EpMjweRD573ASl7uNiHym',
            'Red': '6kZ42qRrzov54LcAk4onW9',
            '1989': '34OkZVpuzBa9y40DCy0LPR',
            'reputation': '6DEjYFkNZh67HP7R9PSZvv',
            'Lover': '1NAmidJlEaVgA3MpcPFYGq',
            'folklore': '1pzvBxYgT6OVwJLtHkrdQK',
            'evermore': '6AORtDjduMM3bupSWzbTSG',
            'Midnights': '1fnJ7k0bllNfL1kVdNVW1A'
            }

"""
def prepare_spotify_query(song):
    song_name = song['Title']
    album_name = song['Album']
    album_id = albumids.get(album_name, '')
    query_base = f"%20track:{song_name.replace(' ', '%20')}%20artist:06HL4z0CvFAxyc27GXpf02%20album:{album_id}%20"
    return query_base
"""
def songid(song):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET))
    album = song['Album']
    if album=='none':
        return(song['id'])
    elif song.get('spotify', True)==False:
        return 'sad'
    else:
        s = sp.album_tracks(album_id=albumids[album])['items'][song['index']-1]
        #print(s['preview_url'])
        return s['id']

def open_song(songid):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_ID,
                                                               client_secret=SPOTIFY_SECRET))
    link =sp.track(track_id=songid)['external_urls']['spotify']
    webbrowser.open(link, new=0)
