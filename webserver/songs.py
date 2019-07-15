# Sophie Johnson
# 11/24/18

import cherrypy
import json
from _song_database import _song_database

# Song controller class
class SongController(object):

    # Constructor
    def __init__(self, sdb=None):
        # Initialize database
        if sdb is None:
            self.sdb = _song_database()
        else:
            self.sdb = sdb 
        # Load songs 
        self.sdb.load_database_info('songData.json')

    # Post a new song 
    def POST_SONG_INDEX(self):
        output = {'result' : 'success'}
        # Attempt to add new song 
        try:
            self.sdb.add_song(cherrypy.request.body.read())
        # Handle exception as error
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

    # Get song information based on song title 
    def GET_SONG_TITLE(self, title):
        output = {'result' : 'success'}
        title = str(title)
        # Attempt to get song information
        try:
            info = self.sdb.get_song_info(title)
            if info:
                output['song'] = info[0] 
                output['year'] = info[1]
                output['artist'] = info[2]
                output['genre'] = info[3]
                output['lyrics'] = info[4]
            else:
                output['result'] = 'error'
                output['message'] = 'Song not found in database.' 
        # Handle exception as error
        except Exception as e:
            output = {}
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

    # Set song information based on title 
    def PUT_SONG_TITLE(self, title):
        output = {'result' : 'success'}
        title = str(title)
        song_dict = json.loads(cherrypy.request.body.read())
        song_dict['song'] = title
        # Attempt to set song information
        try:
            self.sdb.delete_song(title)
            self.sdb.add_song(json.dumps(song_dict))
        # Handle exception as error
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

    # Delete song information based on song id
    def DELETE_SONG_TITLE(self, title):
        output = {'result' : 'success'}
        title = str(title)
        # Attempt to delete song information
        try:
            self.sdb.delete_song(title)
        # Handle exception as error
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)
