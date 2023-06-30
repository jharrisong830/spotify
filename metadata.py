import json

def extract_isrc(library_path: str) -> list[str]:
    '''Extracts each songs' ISRC code from a song library, and returns a list of all codes
    library_path: path to the library file (simple or extended)'''
    with open(library_path) as json_file:
        data = json.load(json_file)
        ids = []
        if list(data[0].keys()) == ["added_at", "track"]:
            for song in data:
                ids.append(song["track"]["external_ids"]["isrc"])
            return ids
        else:
            for song in data:
                ids.append(song["isrc"])
            return ids
    
def extract_song_names(library_path: str) -> list[str]:
    '''Extracts each songs' name from a song library, and returns them as a list
    library_path: path to the library file (simple or extended)'''
    with open(library_path) as json_file:
        data = json.load(json_file)
        song_names = []
        if list(data[0].keys()) == ["added_at", "track"]:
            for song in data:
                song_names.append(song["track"]["name"])
            return song_names
        else:
            for song in data:
                song_names.append(song["name"])
            return song_names
    
def songs_per_artist(library_path: str) -> dict[str, int]:
    '''Returns a dictionary of artists and the number of songs they have in the library
    library_path: path to the library file (simple or extended)'''
    with open(library_path) as json_file:
        data = json.load(json_file)
        dict = {}
        if list(data[0].keys()) == ["added_at", "track"]:
            for song in data:
                track_artists = song["track"]["artists"]
                for artist in track_artists:
                    name = artist["name"]
                    if name in dict: dict[name] += 1
                    else: dict[name] = 1
            return dict
        else:
            for song in data:
                track_artists = song["artists"]
                for artist in track_artists:
                    if artist in dict: dict[artist] += 1
                    else: dict[artist] = 1
            return dict
    
def artists_by_popularity(library_path: str) -> list[list]:
    '''Returns a sorted list of artists based on how many songs they have in a song library
    library_path: path to the library file (simple or extended)'''
    artist_freq = songs_per_artist(library_path)
    list_artist = []
    for key, value in artist_freq.items():
        list_artist.append([key, value])
    list_artist = sorted(list_artist, key=lambda x: x[1], reverse=True)
    return list_artist

def get_songs_by_artist(library_path: str, artist: str):
    '''Returns a list of songs by a given artist from a song library
    library_path: path to the library file (simple or extended)
    artist: name of the artist to search for (must match exactly)'''
    with open(library_path) as json_file:
        data = json.load(json_file)
        songs = []
        if list(data[0].keys()) == ["added_at", "track"]:
            for song in data:
                artists = song["track"]["artists"]
                for name in artists:
                    if artist in name["name"]:
                        songs.append(song["track"]["name"])
                        break
            return songs
        else:
            for song in data:
                artists = song["artists"]
                for name in artists:
                    if artist in name:
                        songs.append(song["name"])
                        break
            return songs
    
def compare_libraries_by_isrc(lib1: str, lib2: str) -> bool:
    '''Returns True if all songs are present in both song libraries, False otherwise
    lib1: path to first song library (simple or extended)
    lib2: path to second song library (simple or extended)'''
    id1 = extract_isrc(lib1)
    id2 = extract_isrc(lib2)
    for x, y in zip(id1, id2):
        if x not in id2: return False
        if y not in id1: return False
    return True



def total_song_time(library_path: str) -> int:
    '''Returns the total time of all songs in the library (in miliseconds)
    library_path: path to the library file (extended required)'''
    with open(library_path) as json_file:
        data = json.load(json_file)
        if list(data[0].keys()) != ["added_at", "track"]:
            raise ValueError("Must use extended metadata")
        total_time = 0
        for song in data:
            total_time += song["track"]["duration_ms"]
        return total_time
    
def total_song_count(library_path: str) -> int:
    '''Returns the total number of songs in the library
    library_path: path to the library file (simple or extended)'''
    with open(library_path) as json_file:
        data = json.load(json_file)
        return len(data)