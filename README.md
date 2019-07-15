# Music Information and Recommendation Service

The OO API provides an interface to obtain useful information from the song database. This readme will describe the functionality provided by the API expected input/output for each API function.

## Functionality

This API allows the user to obtain information about a song including title, year, artist, genre, and lyrics. It also allows the user to obtain a list of songs by a given artist. Further, it allows users to add or delete songs from the database. Finally, it provides recommendations of similar songs or similar artists to the one the user inputs.

## Functions

### load_database_info(self):

This function expects a json file as input. The input file to be used for this project is songData.json. It parses the json data from this file into song and artist dictionaries that will be accessed when receiving information queries. 

### get_song_info(self, title):

This function takes in the title of a song as a string. If the song is in the database, the function will return a list containing [title, year, artist, genre, lyrics]. Otherwise, it will return None.

### get_artist_songs(self, artist):

This function takes in the name of the artist as a string. If the artist is in the database, the function will return a list containing [genre,[songs]]. Otherwise, it will return None.

### add_song(self, song):

This function takes in the song in json format. For example:  
newSong = "{\\"song\\": \\"viva la vida\\", \\"year\\": 2005, \\"artist\\": \\"coldplay\\", \\"genre\\": \\"Pop\\", \\"lyrics\\": \\"sweeping the city streets\\"}"  
The function will then add the song information to the song dictionary and artist dictionary of the database.

### delete_song(self, song):

This function takes in the song title as a string. If the song is in the database, it will delete the song from the song dictionary and the artist dictionary. If this results in the artist having no remaining songs, the artist will also be deleted. 

### recommend_similar_songs(self, title):

This function takes in the song title as a string. If the song is in the database, it will recommend up to 10 randomly selected similar songs based on the music genre. The songs will be returned as a set.

### recommend_similar_artists(self, artist):

This function takes in the artist as a string. If the artist is in the database, it will recommend up to 5 randomly selected similar artists based on the music genre. The artists will be returned as a set.
