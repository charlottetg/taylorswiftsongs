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

def open_song(songid):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_ID,
                                                               client_secret=SPOTIFY_SECRET))
    link =sp.track(track_id=songid)['external_urls']['spotify']
    webbrowser.open(link, new=0)
