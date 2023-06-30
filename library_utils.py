import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json
from song import Song


def get_library():
    load_dotenv()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), redirect_uri=os.getenv("REDIRECT_URI"), scope="user-library-read"))
    all_songs = []
    i = 0
    to_append = sp.current_user_saved_tracks(limit=50, offset=i*50)
    total = to_append["total"]                                          # type: ignore

    while len(all_songs) < total:
        i += 1
        for song in to_append["items"]:                                 # type: ignore
            song["track"].pop("available_markets")
            song["track"]["album"].pop("available_markets")
            song["track"]["album"].pop("images")
            all_songs.append(song)
        to_append = sp.current_user_saved_tracks(limit=50, offset=i*50)

    json_object = json.dumps(all_songs, indent=4)

    with open("songs_extended_metadata.json", "w") as outfile:
        outfile.write(json_object)


def simplify_metadata(library_path: str) -> list[Song]:
    with open(library_path) as json_file:
        data = json.load(json_file)
        song_objs = []
        for song in data:
            song_objs.append(Song(song["track"]["name"],
                                  song["track"]["external_ids"]["isrc"],
                                  [artist["name"] for artist in song["track"]["artists"]],
                                  song["track"]["album"]["name"],
                                  [artist["name"] for artist in song["track"]["album"]["artists"]]))
        json_object = json.dumps([song.to_object() for song in song_objs], indent=4)
        with open("songs.json", "w") as outfile:
            outfile.write(json_object)
        return song_objs





# def add_to_library(isrc_list: list[str]):
#     load_dotenv()
#     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), redirect_uri=os.getenv("REDIRECT_URI"), scope="user-library-read,user-library-modify"))
