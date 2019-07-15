# Sophie Johnson
# 11/24/18

import unittest
import requests
import json

# Test web service 
class TestWebService(unittest.TestCase):

    SITE_URL = 'http://student04.cse.nd.edu:52072'
    RESET_URL = SITE_URL + '/reset/'
    SONGS_URL = SITE_URL + '/songs/'
    ARTISTS_URL = SITE_URL + '/artists/'
    SONG_RECS_URL = SITE_URL + '/recommendations/songs/'
    ARTIST_RECS_URL = SITE_URL + '/recommendations/artists/'

    # Check if json
    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    # Reset data
    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

    # Test reset of all songs and artists in database
    def test_reset_index_put(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

    # Test reset for specific song given title
    def test_reset_title_put(self):
        title = "galway-girl"
        m = {}
        r = requests.put(self.RESET_URL + title, json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
    
    # Test post request to add new song and update artist
    def test_songs_index_post(self):
        self.reset_data()
        title = "new-song"
        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')

        m = {}
        m['song'] = 'new-song' 
        m['year'] = 2018 
        m['artist'] = 'new-artist'
        m['genre'] = 'new-genre'
        m['lyrics'] = 'new-lyrics'
        r = requests.post(self.SONGS_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['song'], title)
        self.assertEqual(resp['year'], m['year'])
        self.assertEqual(resp['artist'], m['artist'])
        self.assertEqual(resp['genre'], m['genre'])
        self.assertEqual(resp['lyrics'], m['lyrics'])

        r = requests.get(self.ARTISTS_URL + m['artist'])
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['artist'], m['artist'])
        self.assertEqual(resp['genre'], m['genre'])
        self.assertEqual(resp['songs'][0], m['song'])
    
    # Test get request for song information
    def test_songs_title_get(self):
        self.reset_data()
        title = "crazy-in-love"
        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['song'], 'crazy-in-love')
        self.assertEqual(resp['year'], 2006)
        self.assertEqual(resp['artist'], 'beyonce-knowles')
        self.assertEqual(resp['genre'], 'Pop')
        self.assertEqual(resp['lyrics'][:10], 'I love you')
    
    # Test put request to update song information
    def test_songs_title_put(self):
        self.reset_data()
        title = "crazy-in-love"
        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['song'], 'crazy-in-love')
        self.assertEqual(resp['year'], 2006)
        self.assertEqual(resp['artist'], 'beyonce-knowles')
        self.assertEqual(resp['genre'], 'Pop')
        self.assertEqual(resp['lyrics'][:10], 'I love you')

        m = {}
        m['year'] = 2018   
        m['artist'] = 'queen-bey'
        m['genre'] = 'r&b'
        m['lyrics'] = 'crazy in loveeeee'
        r = requests.put(self.SONGS_URL + title, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['song'], 'crazy-in-love')
        self.assertEqual(resp['year'], m['year'])
        self.assertEqual(resp['artist'], m['artist'])
        self.assertEqual(resp['genre'], m['genre'])
        self.assertEqual(resp['lyrics'], m['lyrics'])
    
    # Test delete request to delete song
    def test_songs_title_delete(self):
        self.reset_data()
        title = "crazy-in-love"
        m = {}
        r = requests.delete(self.SONGS_URL + title, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
    
    # Test get request for artist information
    def test_artists_name_get(self):
        self.reset_data()
        artist = "beyonce-knowles"
        r = requests.get(self.ARTISTS_URL + artist)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['artist'], artist)
        self.assertEqual(resp['genre'], 'Pop')
        self.assertEqual(resp['songs'][0], 'ego-remix')
    
    # Test get request for song recommendations 
    def test_song_recs_title_get(self):
        self.reset_data()
        title = "crazy-in-love"

        r = requests.get(self.SONGS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        orig_genre = resp['genre']

        r = requests.get(self.SONG_RECS_URL + title)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        for song in resp['song_recommendations']:
            r = requests.get(self.SONGS_URL + song)
            self.assertTrue(self.is_json(r.content.decode('utf-8')))
            resp = json.loads(r.content.decode('utf-8'))
            self.assertEqual(resp['genre'], orig_genre)
    
    # Test get request for artist recommendations 
    def test_artist_recs_title_get(self):
        self.reset_data()
        name = 'beyonce-knowles'

        r = requests.get(self.ARTISTS_URL + name)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        orig_genre = resp['genre']

        r = requests.get(self.ARTIST_RECS_URL + name)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        for artist in resp['artist_recommendations']:
            r = requests.get(self.ARTISTS_URL + artist)
            self.assertTrue(self.is_json(r.content.decode('utf-8')))
            resp = json.loads(r.content.decode('utf-8'))
            self.assertEqual(resp['genre'], orig_genre)

if __name__ == "__main__":
    unittest.main()

