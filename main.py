import library_utils
import metadata
import os






if __name__ == "__main__":
    total_songs = metadata.total_song_count("songs.json")
    total_ms = metadata.total_song_time("songs_extended_metadata.json")
    print(f"Total songs: {total_songs} songs\nTotal Time: {total_ms/1000:.4f} seconds, {total_ms/1000/60:.4f} minutes, {total_ms/1000/60/60:.4f} hours\nAverage Song Time: {(total_ms/1000)/total_songs:.4f} seconds, {(total_ms/1000/60)/total_songs:.4f} minutes")

