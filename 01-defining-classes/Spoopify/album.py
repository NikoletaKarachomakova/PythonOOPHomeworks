from Spoopify.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [s for s in songs]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        if song in self.songs:
            return "Song is already in the album."

    def remove_song(self, song_name: str):
        album_names = [s.name for s in self.songs]
        if song_name not in album_names:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name in album_names:
            index = album_names.index(song_name)
            del self.songs[index]
            return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        if self.published:
            return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"
        return result
