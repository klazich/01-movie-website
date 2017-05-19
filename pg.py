# import media
import pprint
from json import loads
from requests import get

pp = pprint.PrettyPrinter(indent=4)


def log(message):
    pp.pprint(message)


# test = media.Movie('Inception', 'https://youtu.be/YoHD9XEInc0')
# log(test.fetch_movie_data())
OMDB_API_KEY = 'df397f1b'
OMDB_QUERY = 'http://www.omdbapi.com/?apikey={}'.format(OMDB_API_KEY)


def get_movie_imdb_id(movie, year=None):
    request = ''.join([OMDB_QUERY, '&s=', movie.replace(' ', '+')])
    if year is not None:
        request = "".join([request, '&y=', year])

    response = get(request)
    if response:
        log(dir(response))
        log(response.status_code)
        log(response.reason)
        log(response.request)
        log(response.url)
    response_dictionary = loads(response.text)

    if response.ok:
        imdb_id = response_dictionary['Search'][0]['imdbID']
        return imdb_id
    else:
        return None


id = get_movie_imdb_id('mad max', '2015')

log(id)
