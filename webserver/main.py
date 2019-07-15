# Sophie Johnson
# 11/24/18
# Final Project Web Server

import cherrypy

from reset import ResetController
from songs import SongController
from artists import ArtistController 
from recommendations import RecommendationController 

from _song_database import _song_database

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

# Start web server
def start_service():
    # Instantiate movie database object
    sdb_o = _song_database()

    # Instantiate controllers with movie database object
    resetController = ResetController(sdb=sdb_o)
    songController = SongController(sdb=sdb_o)
    recommendationController = RecommendationController(sdb=sdb_o)
    artistController = ArtistController(sdb=sdb_o)

    # Create dispatcher
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # Connect reset with dispatcher
    dispatcher.connect('reset_put_index', '/reset/', controller=resetController, action='PUT_INDEX', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_put_song', '/reset/:song', controller=resetController, action='PUT_SONG', conditions=dict(method=['PUT']))

    # Connect movies with dispatcher
    dispatcher.connect('song_post_index', '/songs/', controller=songController, action='POST_SONG_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('song_get_title', '/songs/:title', controller=songController, action='GET_SONG_TITLE', conditions=dict(method=['GET']))
    dispatcher.connect('song_put_title', '/songs/:title', controller=songController, action='PUT_SONG_TITLE', conditions=dict(method=['PUT']))
    dispatcher.connect('song_delete_title', '/songs/:title', controller=songController, action='DELETE_SONG_TITLE', conditions=dict(method=['DELETE']))

    # Connect artists with dispatcher
    dispatcher.connect('get_artist_name', '/artists/:name', controller=artistController, action='GET_ARTIST_NAME', conditions=dict(method=['GET']))

    # Connect recommendations with dispatcher
    dispatcher.connect('get_recommendation_song_title', '/recommendations/songs/:title', controller=recommendationController, action='GET_RECOMMENDATION_SONGS_TITLE', conditions=dict(method=['GET']))
    dispatcher.connect('get_recommendation_artist_name', '/recommendations/artists/:name', controller=recommendationController, action='GET_RECOMMENDATION_ARTISTS_NAME', conditions=dict(method=['GET']))

    # Connect all with options
    dispatcher.connect('reset_options', '/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('reset_title_options', '/reset/:song', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('songs_options', '/songs/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('songs_title_options', '/songs/:title', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('artists_name_options', '/artists/:name', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('recommendations_songs_title_options', '/recommendations/songs/:title', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('recommendations_artists_name_options', '/recommendations/artists/:name', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))

    # Configuration
    conf = {
        'global' : {
            'server.socket_host' : 'student04.cse.nd.edu',
            'server.socket_port' : 52072,
        },
        '/' : {
            'request.dispatch' : dispatcher,
            'tools.CORS.on' : True
        }
    }
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# Options controller
class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

# Main function
if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
