import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

USER_ID = "your ID"


def get_playlist_id(name):
    playlists = spotify.user_playlists(user=USER_ID)
    for playlist in playlists["items"]:
        if playlist["name"] == name:
            playlist_id = playlist["id"]
            return playlist_id
        else:
            pass


def shuffle_playlist(name):
    playlist_id = get_playlist_id(name)
    tracks = spotify.playlist_items(playlist_id=playlist_id)
    track_list = [track["track"]["id"] for track in tracks["items"]]
    random.shuffle(track_list)

    new_name = f"{name}"
    new_playlist = spotify.user_playlist_create(user=USER_ID, name=new_name, public=True)
    new_playlist_id = new_playlist["id"]

    spotify.playlist_add_items(playlist_id=new_playlist_id, items=track_list)


playlist_name = input("Type in name of the playlist: ")

shuffle_playlist(playlist_name)
