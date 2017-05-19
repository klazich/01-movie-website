"""

"""
import webbrowser
import requests

OMDB_API_KEY = 'df397f1b'
OMDB_URL = 'http://www.omdbapi.com/'


class Movie:
    """

    """

    def __init__(self, movie_title, trailer_youtube, release_year=None):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year

        # self.storyline = movie_storyline
        # self.poster_image_url = poster_image

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_movie_meta(self):
        payload = {'apikey': OMDB_API_KEY,
                   't': self.title,
                   'y': self.release_year}
        response = requests.get(OMDB_URL, params=payload)

        response.raise_for_status()

        return response.json()
