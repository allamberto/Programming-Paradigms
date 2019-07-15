import json
import random

class _song_database:
    def __init__(self):
        self.songs = dict()
        self.artists = dict()

    # loads all the song information into the song dictionary and artist
    # dictionary
    def load_database_info(self, song_file):
        try:
            f = open(song_file)
            song_data = f.read()
            loaded_info = json.loads(song_data)
            for json_song in loaded_info:
                title = json_song['song']
                year = json_song['year']
                artist = json_song['artist']
                genre = json_song['genre']
                lyrics = json_song['lyrics']
                song = {"year": year, "artist": artist, "genre": genre, "lyrics": lyrics}
                self.songs[title] = song
                if not self.artists.get(artist):
                    self.artists[artist] = {"genre": genre, "songs": [title]}
                else:
                    if title not in self.artists[artist]['songs']:
                        self.artists[artist]['songs'].append(title)
            f.close()

        except Exception as e:
            print(e)

    # returns a list of all the information for a given song
    def get_song_info(self,title):
        try:
            song = self.songs[title]
            year = song['year']
            artist = song['artist']
            genre = song['genre']
            lyrics = song['lyrics']
            return [title, year, artist, genre, lyrics]

        except KeyError:
            print("Song not found in database")
            return None

    # returns a list of all the songs by the given artist
    def get_artist_songs(self,artist):
        try:
            artist_info = self.artists[artist]
            genre = artist_info['genre']
            songs = artist_info['songs']
            return [genre, songs]

        except KeyError:
            print("Artist not found in database")
            return None

    # returns a set of up to 10 random song recommendations of similar songs
    # based on genre of given song
    def recommend_similar_songs(self,title):
        try:
            song = self.songs[title]
            artist = song['artist']
            genre = song['genre']
            similar_songs = []
            for key, value in self.songs.items():
                if value['genre'] == genre and value['artist'] !=  artist and key != title:
                    similar_songs.append(key)

            recommendations = set()
            if len(similar_songs) > 10:
                set_size = 10
            else: 
                set_size = len(similar_songs)
            while len(recommendations) < set_size:
                index = random.randint(0,len(similar_songs)-1);
                recommendations.add(similar_songs[index]);
            return recommendations

        except KeyError:
            print("Song not found in database")
            return None

    # returns a set of up to 5 random recommendations of similar artists based
    # on genre of given artist
    def recommend_similar_artists(self, artist):
        try:
            artist_info = self.artists[artist]
            genre = artist_info['genre']
            similar_artists = []
            for key, value in self.artists.items():
                if value['genre'] == genre and key != artist:
                    similar_artists.append(key)

            recommendations = set()
            if len(similar_artists) > 5:
                set_size = 5
            else: 
                set_size = len(similar_artists)
            while len(recommendations) < set_size:
                index = random.randint(0,len(similar_artists)-1);
                recommendations.add(similar_artists[index]);
            return recommendations

        except KeyError:
            print("Artist not found in database")
            return None

    # adds information for a song to the song dictionary and the artist
    # dictionary
    def add_song(self, song):
        try:
            song_info = json.loads(song)
            title = song_info['song']
            year = song_info['year']
            artist = song_info['artist']
            genre = song_info['genre']
            lyrics = song_info['lyrics']
            song = {"year": year, "artist": artist, "genre": genre, "lyrics": lyrics}
            self.songs[title] = song
            if not self.artists.get(artist):
                self.artists[artist] = {"genre": genre, "songs": [title]}
            else:
                if title not in self.artists[artist]['songs']:
                    self.artists[artist]['songs'].append(title)

        except Exception as e:
            print(e)

    # deletes song information from song dictionary and artist dictionary.
    # if this leaves the artist with 0 songs, the artist is deleted
    def delete_song(self, title):
        try:
            print("in delete_song")
            artist = self.songs[title]['artist'] 
            del self.songs[title]
            self.artists[artist]['songs'].remove(title)
            if len(self.artists[artist]['songs']) == 0:
                print("deleting artist")
                del self.artists[artist]

        except Exception as e:
            print(e)

    # reset database 
    def reset_database(self):
        self.songs.clear()
        self.artists.clear()

if __name__ == "__main__":
    sdb = _song_database()
    sdb.load_database_info("./songData.json")
    artist = sdb.get_artist_songs("buckcherry")
    newSong = "{\"song\": \"viva la vida\", \"year\": 2005, \"artist\": \"coldplay\", \"genre\": \"Pop\", \"lyrics\": \"sweeping the city streets\"}"
    sdb.add_song(newSong)
    song = sdb.get_song_info("galway-girl")
    #print(song)
    artist = sdb.get_artist_songs("celtic-thunder")
    #print(artist)
    print(len(artist[1]))
    sdb.delete_song("viva la vida")
    song = sdb.get_song_info("viva la vida")
    print(song)
    artist = sdb.get_artist_songs("coldplay")
    print(artist)
    recommendations = sdb.recommend_similar_artists("celtic-thunder")
    print(recommendations)
