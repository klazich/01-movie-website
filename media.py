"""

"""
# OMDB API
# http://www.omdbapi.com/?apikey=[yourkey]&
# api_key: "df397f1b"

# import json, requests
# url = "http://www.omdbapi.com/?t=scream"
# response = requests.get(url)
# python_dictionary_values = json.loads(response.text)

# The Movie Database API
# api_key: "4ba86a24d84ecbf254b1cee306e0f9ed"
# example:
#     https://api.themoviedb.org/3/movie/550?api_key=4ba86a24d84ecbf254b1cee306e0f9ed

# goo.gl api
# api_key: "AIzaSyBnC_nAB4UbOJCvhZ52rX8X92N1V1Tgeto"

# youtube api
# api_key: "AIzaSyBlr3kG98VwGz5D3QufXG2dqXgj6HDnwpQ"

# Google API Pyhton Client
# run: pip install --upgrade google-api-python-client

import webbrowser
import json
import requests


class Movie():
    def __init__(self, movie_title, movie_storyline=None, poster_image=None, trailer_youtube=None):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def __fetch_movie_data(self):
        query_string = 'http://www.omdbapi.com/?t=%s' % (self.movie_title)
