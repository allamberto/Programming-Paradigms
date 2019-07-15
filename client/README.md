# Music Information and Recommendation Service
---
## GUI Link: [Music RecommeNDer](http://student04.cse.nd.edu/alamber2/Wsyebf763/client_1/)

This web client allows simple interaction with our RESTful API and web
server. This document describes instructions for the user regarding both the GUI
and running of the server.

---
## Functionality
 
This web client allows users to obtain information about songs including title,
year made, genre, artist, and lyrics. Using the user interface, one can:
1) Look up a specific song by searching for the title - Recieve information
about song artist, genre, year made, lyrics, and ten other song recommendations based on
similar genres.
2) Look up a specic artist by searching for the artist's name - Recieve
information about genre, songs by the artist in the data base, and five other song
reocommendations based on the genre.

Note: To search titles or artists, one must type in request in all lowercase
letters with dashes instead of spaces. Example: "arcade-fire"

3) Add a song to the song database.
4) Remove a song from the song database.
5) Reset the database to its original state.

---
## Run The Server

To run the server, navigate to the [webserver
branch](https://gitlab.com/sophiejohnson/paradigms_project/tree/webserver/webserver) and download all the
necessary files: _song_database.py, artists.py, main.py, recommendations.py,
reset.py, songData.json, songs.py, test_ws.py. Once these files are downloaded,
test_ws.py can be used to check their functionality. If these files pass all the
tests, the server can be started by executing the main.py file with the correct
form of python, which can be found at
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python.

---
Once the server is running, go to the above GUI link to use the webclient. Happy
RecommeNDing!

--- 
## Side Note: Testing

The best way to test this user interface is to use it to its full capability.
Search for songs that are already in the database to make sure the GET request
returns success (aka finds the song). Search for artists in the same manner. Add
a song to the database and search for it to check that the PUT request is
working. Then, delete the song and search for it again to test that the DELETE
request is working. Lastly, add a song again and use the reset button to reset
the databse to its original state. Search for that song to confirm that the PUT
request in the reset class is working. Once all these aspects are tested in this
way, the functionality of the program has been confirmed. 
