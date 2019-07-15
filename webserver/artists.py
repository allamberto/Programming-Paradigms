# Sophie Johnson
# 11/24/18

import cherrypy
import json
from _song_database import _song_database

# Artist controller class
class ArtistController(object):

    # Constructor
    def __init__(self, sdb=None):
        # Initialize database
        if sdb is None:
            self.sdb = _song_database()
        else:
            self.sdb = sdb 
        # Load songs 
        self.sdb.load_database_info('songData.json')

    # Get artist information based on name 
    def GET_ARTIST_NAME(self, name):
        output = {'result' : 'success'}
        name = str(name)
        # Attempt to get artist information
        try:
            info = self.sdb.get_artist_songs(name)
            if info:
                output['artist'] = name 
                output['genre'] = info[0] 
                output['songs'] = info[1]
            else:
                output['result'] = 'error'
                output['message'] = "Artist not found in database." 
        # Handle exception as error
        except Exception as e:
            output = {}
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)
