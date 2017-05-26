<!-- Badges -->

<p>
    <img src="https://github.com/klazich/01-movie-website/blob/master/images/udacity-logo.png?raw=true"
         alt="Udacity"
         align="middle">
    <img src="https://img.shields.io/badge/python-2.7-blue.svg"
         alt="Python27"
         align="right">
</p>

<!--
 ##### README [checklist](https://github.com/noffle/art-of-readme)
 - [x] One-liner explaining the purpose of the module
 - [ ] Necessary background context & links
 - [ ] Potentially unfamiliar terms link to informative sources
 - [x] Clear, *runnable* example of usage
 - [ ] Installation instructions
 - [x] Extensive API documentation
 - [ ] Performs [cognitive funneling](https://github.com/noffle/art-of-readme#cognitive-funneling)
 - [x] Caveats and limitations mentioned up-front
 - [x] Doesn't rely on images to relay critical information
 - [ ] License
-->

###### *Created for the Move Website project while taking the Udacity Full Stack Web Development Nanodegree*

# class-movie-website

> Generates HTML for a movie trailer website using a simple and flexible movie data structure with optional
  client APIs to assist information retrieval.

**class-movie-website** does 3 things:

 1. Provides a simple and flexible Python class, [`Movie`](#movie-instantiation) to handle movie data.
The Movie class, using the `get_movie_data` static method, queries OMDB for movie info and YouTube for the
movie trailer.

## Usage

#### Import the class

```python
from media import Movie
```

#### Creating a Movie instance

```python
INCEPTION = Movie('Inception',
                  'A thief, who steals corporate secrets through use of dream-sharing '
                  'technology, is given the inverse task of planting an idea into the '
                  'mind of a CEO.',
                  'https://www.youtube.com/watch?v=YoHD9XEInc0',
                  'https://goo.gl/NK7fvQ')
```

#### Useing `Movie.get_movie_data` to fetch movie info from OMDB and YouTube

```python
# pass in the release year to narrow searches
MAD_MAX_DATA = Movie.get_movie_data('Mad Max', '2015')
MAD_MAX = Movie(MAD_MAX_DATA['title'],
                MAD_MAX_DATA['plot'],
                MAD_MAX_DATA['youtube_url'],
                MAD_MAX_DATA['poster'],
                MAD_MAX_DATA)
```

#### Useing `Movie.movie` to fetch data and create an instance in one line

```python
PRIMER = Movie.movie('Primer')
```
`Movie.movie` also accepts a second argument `year` to narrow searches
```python
BLADE_RUNNER = Movie.movie('Blade Runner', '1982')
```

#### HTML can then be generated and opened in a web browser

```python
from fresh_tomatoes import open_movies_page

MOVIES = [INCEPTION, MAD_MAX, PRIMER, BLADE_RUNNER]
open_movies_page(MOVIES)
```


## On OMDB and YouTube API client authentication

The class Movie exposes [two static methods](#methods) that can be use to assist
in obtaining the data needed to create a Movie object.

**Note:** The querying features of the Movie class need API keys to
authenticate calls to YouTube and omdbapi.com services. These features are optional.

> API key information:
> - Information on how Google's APIs handles authentication and authorization is
available in the [Google API Client Library for Python](https://developers.google.com/api-client-library/python/start/get_started) documentation.
> - Information on obtaining an OMDB API key can be found at there website
[omdbapi.com](http://www.omdbapi.com/).


## API
- **media.py**
    - [Movie class instantiation](#movie-instantiation)
        - Movie()
        - Movie.movie()
    - [Movie attributes and methods](#movie-attributes-and-methods)
        - [Atrributes](#attributes)
            - m.title
            - m.plot
            - m.trailer_youtube_url
            - m.poster_image_url
            - m.info
        - [Methods](#methods)
            - m.show_trailer()
            - m.show_poster()
            - *static* Movie.get_movie_data()
            - *static* Movie.movie()
1. [Search](#search)
    - youtube_search()
    - omdb_search()
1. [Fresh Tomatoes](#fresh-tomatoes)
    - open_movies_page()

### [media.py](./media.py)

#### Movie instantiation

There are two ways to create a `Movie` object:
1. via the `Movie` class constructor
2. via a static method, `Movie.movie` that first [fetches movie data](#search)
   required and returns a new Movie instance.

#### `m = Movie(title, plot, youtube_url, image_url, movie_data=None)`
> `m` being the new instance of Movie

- `title` (*required*) - The movie's title
- `plot` (*required*) - The movie's plot/storyline
- `youtube_url` (*required*) - A URL to a video of a movie trailer on YouTube
- `image_url` (*required*) - A URL to an image of a movie poster or box art
- `movie_data` (*optional*) - A Python dictionary<sup>[1](#footnote-1)</sup>
  of additional movie information

#### `m = Movie.movie(movie_title, year=None)`
> `m` being the new instance of Movie

- `movie_title` (*required*) - The movie's title (used in API queries)
- `year` (*optional*) - The movie's release year (used in API queries)
    > Helpful when there are several movies of the same name. Such as 'Mad Max',
      If you wanted the original, `year` would be `'1979'`. Or, `'2015'` for
      the newer release.

#### Movie attributes and Methods

> **Note:** *the variable* `m` *is an instance of* `Movie`.

##### Attributes

- **`m.title`** (*str*) - The movie title.
- **`m.plot`** (*str*) - The movie plot.
- **`m.trailer_youtube_url`** (*str*) - YouTube URL to a movie tralier.
- **`m.poster_image_url`** (*str*) - A URL to image of movie poster or box art.
- **`m.info`** (*dict*) - A dictionary<sup>[1](#footnote-1)</sup> of additional movie data.

##### Methods

- **`m.show_trailer()`** - Opens the URL saved to `trailer_youtube_url` in a web browser.
- **`m.show_poster()`** - Opens the URL saved to `poster_image_url` in a web browser.
- *static* **`Movie.get_movie_data(movie_title, year=None, *queries)`**
    - `movie_title` (*required*) - The movie's title.
    - `year` (*optional*) - The movie's release year.
    - `*queries` (*optional;variadic<sup>[2](#footnote-2)</sup>*) - A variable number of additional query terms.

### [search.py](./search.py)

- `youtube_search(dev_key)`

- `omdb_search(dev_key)`

### [fresh_tomatoes.py](./fresh_tomatoes.py)

- `open_movies_page([Movie, ...])`

## Installation

## Todo
- [ ] :exclamation:Testing!!!
- [ ] Upload project to PyPi for easy installation with pip.
- [ ] HTML and CSS customization options.

## Footnotes

1. <a name="footnote-1"></a>
   [Python Data Structures - Dictionaries](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries)
2. <a name="footnote-2"></a>
   [Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)



## Licence

MIT License

Copyright (c) 2017 Kevin W. Lazich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.