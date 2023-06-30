class Song:
    def __init__(self, name: str="", isrc: str="", artists: list[str]=[], album_name: str="", album_artists: list[str]=[]):
        self.name = name
        self.isrc = isrc
        self.artists = artists
        self.album_name = album_name
        self.album_artists = album_artists
    
    def to_object(self) -> dict:
        return {
            "name": self.name,
            "isrc": self.isrc,
            "artists": self.artists,
            "album_name": self.album_name,
            "album_artists": self.album_artists
        }
    
    def from_object(self, obj: dict):
        self.name = obj["name"]
        self.isrc = obj["isrc"]
        self.artists = obj["artists"]
        self.album_name = obj["album_name"]
        self.album_artists = obj["album_artists"]

    
    def __str__(self):
        return f"\"{self.name}\" by {self.artists}"
    
