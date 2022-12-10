import random
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

USER_ID = "USER_ID"

# auth_manager = SpotifyClientCredentials()
# spotify = spotipy.Spotify(auth_manager=auth_manager)


def get_playlist_id(playlist_name):
    playlists = spotify.user_playlists(user=USER_ID)
    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            playlist_id = playlist["id"]
            return playlist_id
        else:
            pass


def shuffle_playlist(playlist_name):
    playlist_id = get_playlist_id(playlist_name)
    tracks = spotify.playlist_items(playlist_id=playlist_id)
    track_list = [track["track"]["id"] for track in tracks["items"]]
    random.shuffle(track_list)

    new_name = f"{playlist_name}"
    new_playlist = spotify.user_playlist_create(user=USER_ID, name=new_name, public=True)
    new_playlist_id = new_playlist["id"]

    spotify.playlist_add_items(playlist_id=new_playlist_id, items=track_list)


shuffle_playlist("Playlist name")
