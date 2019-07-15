# Music Information and Recommendation Service

### Port Number: 52072

This RESTful web server allows clients to use GET, PUT, POST, and DELETE requests to obtain and modify song information using the object oriented API. This document describes the resource specification for the server with expected input and output.

## Functionality

This server allows clients to obtain information about a song including its title, year, artist, genre, and lyrics. The server also provides access to a list of all songs by a given artist. It gives song and artist recommendations given a song title and artist name respectively. Finally, clients can modify the existing song information by adding new songs, updating existing titles, deleting records, and reseting the database. 

JSON Guide
[Here](https://docs.google.com/document/d/1nUkxfg3HCHhT7YDQdIupWOGhSot2Qsf1wJqjEdJEsGM/edit?usp=sharing)

## Run The Server

To run the server, navigate to the [webserver
branch](https://gitlab.com/sophiejohnson/paradigms_project/tree/webserver/webserver)
and download all the
necessary files: _song_database.py, artists.py, main.py, recommendations.py,
reset.py, songData.json, songs.py, test_ws.py. Once these files are downloaded,
test_ws.py can be used to check their functionality. If these files pass all the
tests, the server can be started by executing the main.py file with the correct
form of python, which can be found at
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python.

# Resource Requests

### POST /songs/ 

To add a new song to the database, a client can send a POST request to the endpoint /songs/. This functionality was included to allow the user to expand the existing database with new song additions.  The body for the request should contain a JSON string with values for the keys "song", "year", "artist", "genre", and "lyrics". The server reponse indicates whether the result is "success" or "failure".

Example Input: `{"song": "viva-la-vida", "year": 2005, "artist": "coldplay", "genre": "Pop", "lyrics": "Sweeping the city streets..."}`

Example Output: `{"result": "success"}`

### GET /songs/:title

A GET request to the endpoint /songs/:title returns a JSON string with the song information. The request depends upon the song's title so that a user can search based on the title of the song. This pieces of information is typically known and can be used to get lesser known information. Specifically, the title, year, artist, genre, and lyrics are returned.

Example Output: `{"result": "success", "song": "crazy-in-love", "year": 2006, "artist": "beyonce-knowles", "genre": "Pop", "lyrics": "I love you\n...}`

### PUT /songs/:title

A client can modify a song in the database by sending a PUT request to the endpoint /songs/:title. In addition to adding new songs to the database, this allows users to be able to make changes to existing songs. The body of this request must contain the updated information as a JSON string with values for "year", "artist", "genre", and "lyrics". If the song title is not in the database yet, it will create a new song. Otherwise, it will update the existing entry. The response JSON indicates whether the operation was successful.

Example Input: `{"year": 2018, "artist": "queen-bey", "genre": "r&b", "lyrics": "Crazy in love..."}`

Example Output: `{"result": "success"}`

### DELETE /songs/:title

DELETE requests to the endpoint /songs/:title simply delete the song's entry from the database. A website which offers music recommendations must be able to control which songs are in the database so deletion is possible. Again, response JSON specifies "success" or "failure".

Example Output: `{"result": "success"}`

### GET /artists/:name

A GET request to the endpoint /artists/:name returns a JSON string with information about the artist. While most users will be able to search songs by the title, this additional functionality allows the user to find all songs by a specific artist. Once again, the most commonly known piece of information, the artist's name, is used to provide additional details. Specifically, the artist, genre, and a list of all of the artist's songs in the database are returned.

Example Output: `{"result": "success", "artist": "beyonce-knowles", "genre": "Pop", "songs": ["ego-remix", "then-tell-me", "honesty"...]}`

### GET /recommendations/songs/:title

To get song recommendations based on a given song, a GET request can be sent to the endpoint /recommendations/songs/:title. Based on the genre of the selected song, the server will return JSON which contains a list of song recommendations. Recommendations based on the specific song will provide a wide range of options from many different artists. Then, a GET request can be made with the song title to get more information.

Example Output: `{"result": "success", "song_recommendations": ["be-gentle-with-me", "whiskey-in-the-jar", "my-love-is-like-a-red-red-rose"...]}`

### GET /recommendations/artists/:name

Artist recommendations can also be generated based on a given artist; a GET request sent to the endpoint /recommendations/artists/:name returns JSON with a list of five artists of similar genre. Unlike the recommendations based on song title, these recommendations will provide a broader recommendation rather than listing specific tracks. This recommendation feature is intended to be used in conjunction with the GET request for artist information. After an artist has been recommended, a request can be made to see all of the artist's songs.

Example Output: `{"result": "success", "artist_recommendations": ["geographer", "all-caps", "the-casket-girls"...]}`

### PUT /reset/

A PUT request to the endpoint /reset/ will reload the initial song and artist information for the entire database. TIt is important to be able to return the database to its original state in case unintentional modifications are made. This will return JSON indicating success or failure.

Example Output: `{"result": "success"}`

### PUT /reset/:title

To reset a specific song, a PUT request can be sent to the endpoint /reset/:title. Again, the response will reveal whether the song information was successfully updated in the database. Being able to reset a single song eliminates the need to reset the entire database each time a mistake is made.

Example Output: `{"result": "success"}`
