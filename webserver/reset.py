# Sophie Johnson
# 11/24/18

import cherrypy
import json
from _song_database import _song_database

# Recommendations class
class RecommendationController(object):

    # Constructor
    def __init__(self, sdb=None):
        # Initialize database
        if sdb is None:
            self.sdb = _movie_database()
        else:
            self.sdb = sdb 

    # Retrieve song recommendations given title 
    def GET_RECOMMENDATION_SONGS_TITLE(self, title):
        output = {'result' : 'success'}
        title = str(title)
        # Attempt to get recommendation
        try:
            songs = self.sdb.recommend_similar_songs(title)
            if songs:
                output['song_recommendations'] = list(songs)
            else:
                output['result'] = 'error'
                output['message'] = "Song not found in database." 
        # Handle exception as error
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

    # Retrieve song recommendations given title 
    def GET_RECOMMENDATION_ARTISTS_NAME(self, name):
        output = {'result' : 'success'}
        name = str(name)
        # Attempt to get recommendation
        try:
            artists = self.sdb.recommend_similar_artists(name)
            if artists:
                output['artist_recommendations'] = list(artists)
            else:
                output['result'] = 'error'
                output['message'] = "Artist not found in database." 
        # Handle exception as error
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)
