# class-movie-website

> Generates HTML for a movie trailer website using a simple and flexible movie 
data structure with optional client APIs to assist information retrieval.

`class-movie-website` provides a simple and flexible Python class when working
with movie data. The Movie class, using the `.get_movie_data` static method, 
queries OMDB for movie info and YouTube for the movie trailer.


> **Note:** The querying features of the Movie class need API keys to 
authenticate calls to YouTube and omdbapi.com services. These features are optional.
> - Information on how Google's APIs handles authentication and authorization is
available in the [Google API Client Library for Python](https://developers.google.com/api-client-library/python/start/get_started) documentation.
> - Information on obtaining an OMDB API key can be found at there website
[omdbapi.com](http://www.omdbapi.com/).

## Usage

#### Create a Movie instance

```python
from media import Movie

INCEPTION = Movie('Inception',
                  'A thief, who steals corporate secrets through use of dream-sharing ' 
                  'technology, is given the inverse task of planting an idea into the ' 
                  'mind of a CEO.',
                  'https://www.youtube.com/watch?v=YoHD9XEInc0',
                  'https://goo.gl/NK7fvQ')
```

#### Use `Movie.get_movie_data` to fetch movie info from OMDB and YouTube

```python
from media import Movie

MAD_MAX_DATA = Movie.get_movie_data('Mad Max', '2015')  # pass in the release
MAD_MAX = Movie(MAD_MAX_DATA['title'],                  # year to narrow query
                MAD_MAX_DATA['plot'],
                MAD_MAX_DATA['youtube_url'],
                MAD_MAX_DATA['poster'],
                MAD_MAX_DATA)
```

#### Use `Movie.movie` to fetch data and create instance in one line

```python
from media import Movie

PRIMER = Movie.movie('Primer')
# `Movie.movie` also accepts a second argument `year` to narrow a query:
BLADE_RUNNER = Movie.movie('Blade Runner', '1982')
```