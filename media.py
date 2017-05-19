"""

"""
# OMDB API
# http://www.omdbapi.com/?apikey=[yourkey]&
# api_key: "df397f1b"

# import json, requests
# url = "http://www.omdbapi.com/?t=scream"
# response = requests.get(url)
# python_dictionary_values = json.loads(response.text)

# goo.gl api
# api_key: "AIzaSyBnC_nAB4UbOJCvhZ52rX8X92N1V1Tgeto"

# youtube api
# api_key: "AIzaSyBlr3kG98VwGz5D3QufXG2dqXgj6HDnwpQ"


from webbrowser import open
from json import loads
from requests import get

OMDB_API_KEY = 'df397f1b'
OMDB_QUERY = 'http://www.omdbapi.com/?apikey={}'.format(OMDB_API_KEY)


def get_movie_imdb_id(movie, year=None):
    request = ''.join([OMDB_QUERY, '&s=', movie.replace(' ', '+')])
    if year is not None:
        request = "".join([request, '&y=', year])

    response = get(request)

    response_dictionary = loads(response.text)

    if response_dictionary['Response'] == 'True':
        imdb_id = response_dictionary['Search'][0]['imdbID']
        return imdb_id
    else:
        return None


class Movie:
    """
    
    """

    def __init__(self, movie_title, trailer_youtube, release_year=None):
        """

        Args:
            movie_title (str): The title of the movie
            trailer_youtube (str): A youtube URL to a trailer of the movie 
            release_year (:obj:`str`, optional): 
        """
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube

        # self.storyline = movie_storyline
        # self.poster_image_url = poster_image

    def show_trailer(self):
        open(self.trailer_youtube_url)

    def _fetch_movie_data(self):
        # a request for movie mad max, year 2015
        # http://www.omdbapi.com/?t=mad+max&y=2015
        url_query = 'http://www.omdbapi.com/?t={}'.format(self.title)
        response = get(url_query)
        res_dict = loads(response.text)
        return res_dict
