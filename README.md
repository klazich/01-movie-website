<p>
  <a href="https://www.Udacity.com">
  <img src="https://github.com/klazich/01-movie-website/blob/master/images/udacity-logo.png?raw=true"
       alt="Udacity"
       align="middle">
  </a>
<img src="https://img.shields.io/badge/python-2.7-blue.svg"
       alt="Python27"
       align="middle">
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
 - [x] License
-->

###### *Created for [Udacity](https://www.udacity.com)'s Full Stack Web Development Nanodegree Movie Website project*

# class-movie-website

> Generate HTML for a movie review website using a simple and flexible Python
class to handle movie data and place API request tailored for movie data
retrieval.

class-movie-website does 3 things:

1. Provides a simple and flexible Python class, [**Movie()**](#api) to handle
   movie data.

2. The Movie class also provides access to OMDB and YouTube APIs if additional
   data retrieval is needed.
   > For details on OMDB and YouTube API functionality see
   > [get_movie_data](#static-movieget_movie_datamovie_title-yearnone-queries)
   > and [OMDB and YouTube API](#omdb-and-youtube-api).

3. Given a list of Movie class objects [Fresh Tomatoes](#fresh_tomatoespy) will
   generated the HTML for a movie review web page featuring the provided movies.


## Usage

### Import the class

```python
from media import Movie
```

### Creating a Movie instance

```python
INCEPTION = Movie('Inception',
                  'A thief, who steals corporate secrets through use of' 
                  ' dream-sharing technology, is given the inverse task of'
                  ' planting an idea into the mind of a CEO.',
                  'https://www.youtube.com/watch?v=YoHD9XEInc0',
                  'https://goo.gl/NK7fvQ')
```

### Using `Movie.get_movie_data` to fetch movie info from OMDB and YouTube[*](#omdb-and-youtube-api)

```python
# pass in the release year to narrow searches
MAD_MAX_DATA = Movie.get_movie_data('Mad Max', '2015')
MAD_MAX = Movie(MAD_MAX_DATA['title'],
                MAD_MAX_DATA['plot'],
                MAD_MAX_DATA['youtube_url'],
                MAD_MAX_DATA['poster'],
                MAD_MAX_DATA)
```

### Using `Movie.movie` to fetch data and create an instance in one line

```python
PRIMER = Movie.movie('Primer')
```

`Movie.movie` *also accepts a second argument* `year` *to narrow searches:*

```python
BLADE_RUNNER = Movie.movie('Blade Runner', '1982')
```

### HTML can then be generated and opened in a web browser

```python
from fresh_tomatoes import open_movies_page

MOVIES = [INCEPTION, MAD_MAX, PRIMER, BLADE_RUNNER]
open_movies_page(MOVIES)
```


## API

- **media.py**
  - [Movie()](#movie-instantiation)
    - Construction
      - [m = Movie()](#m--movietitle-plot-youtube_url-image_url-movie_datanone)
    - [Attributes](#attributes)
      - m.title
      - m.plot
      - m.trailer_youtube_url
      - m.poster_image_url
      - m.info
    - Methods
      - [m.show_trailer()](#mshow_trailer)
      - [m.show_poster()](#mshow_poster)
      - [Movie.get_movie_data()](#static-movieget_movie_datamovie_title-yearnone-queries)
      - [Movie.movie()](#static-m--moviemoviemovie_title-yearnone)
- **search.py**
  - [youtube_video_id()](#youtube_video_idtitle-args)
  - [omdb_movie_info()](#omdb_movie_infotitle-yearnone)
- **fresh_tomatoes.py**
  - [open_movies_page()](#open_movies_pagemovie)

### [media.py](./media.py)

#### Movie instantiation

There are two ways to create a `Movie` object:
1. via the `Movie` class constructor
2. via a static method, `Movie.movie` that first [fetches movie data](#searchpy)
   and returns a new Movie instance using retrieved data.

##### m = Movie(title, plot, youtube_url, image_url, movie_data=None)

> **m** being the new instance of Movie

- **title** <sub>*[str]*</sub> (*required*) - The movie's title
- **plot** <sub>*[str]*</sub> (*required*) - The movie's plot/storyline
- **youtube_url** <sub>*[str]*</sub> (*required*) - A URL to a video of a movie
  trailer on YouTube
- **image_url** <sub>*[str]*</sub> (*required*) - A URL to an image of a movie
  poster or box art
- **movie_data** <sub>*[dict]*</sub> (*optional*) - A Python
  dictionary<sup>[1](#footnote-1)</sup> of additional movie information


#### Attributes

> **Note:** *the variable* **m** *is an instance of* **Movie**.

| | Type | Description   |
|---|:---:|---|
| m.title               | *[str]*  |The movie's title.|
| m.plot                | *[str]*  |The movie's plot.|
| m.trailer_youtube_url | *[str]*  |YouTube URL to a movie trailer.|
| m.poster_image_url    | *[str]*  |A URL to image of movie poster or box art.|
| m.info                | *[dict]* |A dictionary<sup>[1](#footnote-1)</sup> of additional movie data.|


#### Methods

##### **m.show_trailer()**

Opens the URL `trailer_youtube_url` in a web browser.

##### **m.show_poster()**

Opens the URL `poster_image_url` in a web browser.

##### *`static`* **Movie.get_movie_data(movie_title, year=None, \*queries)**

- **movie_title** <sub>*[str]*</sub> (*required*) - The movie's title.
- **year** <sub>*[str]*</sub> (*optional*) - The movie's release year.
- **\*queries** <sub>*[str]*</sub>
  (*optional;variadic<sup>[2](#footnote-2)</sup>*) - A variable number of
  additional query terms.

Returns a dictionary with movie data provided by YouTube and OMDB API queries
regarding movie_title, year and any additional queries.

##### *`static`* m = Movie.movie(movie_title, year=None)

- **m** - Instance of class Movie.
- **movie_title** <sub>*[str]*</sub> (*required*) - The movie's title (used in API
  queries)
- **year** <sub>*[str]*</sub> (*optional*) - The movie's release year (used in API
  queries)
    > Helpful when there are several movies of the same name, such as *Mad Max*.
    If we wanted the original film, `year` would be `'1979'`. Or, `'2015'` for
    the newer release.

A shortcut to creating a Movie object from data fetched by `get_movie_data`.
This method calls `get_movie_data` with the arguments passed, and returns a
Movie instance constructed with that data.


### [search.py](./search.py)

##### youtube_video_id(title, \*args)
> A [YouTube API key](#footnote-3) is required for this to function.

- **title** <sub>*[str]*</sub> (*required*) - The movie's title for the search
  query.
- **\*args** <sub>*[str]*</sub> (*optional*) - A variable number of additional
  query terms (such as *year*).

Builds a YouTube API service object and places API search calls tailored for
movie trailer queries and returns a YouTube video id.

##### omdb_movie_info(title, year=None)
> A [omdbapi.com API key](#footnote-4) is required for this to function.

- **title** <sub>*[str]*</sub> (*required*) - The movie's title to search for.
- **year** <sub>*[str]*</sub> (*optional*) - The movie's release year to search
  for.

Places HTTP GET request to omdbapi.com using the Python package [requests](http://docs.python-requests.org/en/master/).
Returns a dictionary<sup>[1](#footnote-1)</sup> containing various information
related to movie query (see [examples.py](./examples.py) for an example of what
this dictionary looks like.).

### [fresh_tomatoes.py](./fresh_tomatoes.py)

##### open_movies_page(\[*Movie\])

- \[*Movie\]
  <sub>[list]\(\*[Movie](#m--movietitle-plot-youtube_url-image_url-movie_datanone)\)</sub>
  (*required*) \- A list of Movie objects.

Generates the HTML for website in projects root directory and using the
[webbrowser](https://docs.python.org/2/library/webbrowser.html) library, opens
the site in a browser window.

> See the file [entertainment_center.py](./entertainment_center.py) for an
> example of how `open_movies_page` is used.


## OMDB and YouTube API

The Movie class exposes a static method,
[`get_movie_data`](#static-movieget_movie_datamovie_title-yearnone-queries) that
uses two api clients from [search.py](./search.py). A YouTube API client and a
omdbapi.com HTTP client to fetch movie data and statistics as well as a link to
a YouTube video of the movie trailer. This functionality is optional and shouldn't
break the class if not used ([their has been very little testing](#todo)).

##### YouTube API
 - Follow the steps listed [here](https://developers.google.com/api-client-library/python/start/get_started#setup).
##### omdbapi.com API
 - Information can be found [here](https://www.omdbapi.com).

> I will be pushing a config.py file with API keys to this projects GitHub repo
> before submitting my project so everything in media.py and search.py will work.
> I know having API keys on a public repo is nono so they will be deactivated in
> a few weeks.



## Installation

**Note:** The following steps assume that you have [**Python**](https://www.python.org/downloads/) 2.7,
[**git**](https://git-scm.com/downloads) and [**pip**](https://pypi.python.org/pypi/pip?),
and know how to use **git clone** and **pip install**.
  > I also like [Anaconda](https://www.continuum.io/downloads)'s bundled Python
    build.

- Fire up a shell and clone https://github.com/klazich/class-movie-website.git
    ```bash
    $ git clone https://github.com/klazich/class-movie-website.git
    ```
- Move into the root:
    ```bash
    $ cd class-movie-website
    ```
- Be sure you have these packages installed if planning to use
[`Movie.get_movie_data`](#static-movieget_movie_datamovie_title-yearnone-queries):
    ```pip
    $ pip install --upgrade requests google-api-python-client 
    ```
- For examples on how to use the Movie class take a look at [examples.py](./examples.py)
  and run:
    ```bash
    $ python examples.py
    ```
- For an example on how to use `open_movies_page` to generate and open HTML see
  [entertainment_center.py](./entertainment_center.py) and run:
    ```bash
    $ python entertainment_center.py
    ```

## Todo

- [ ] :exclamation:Testing:exclamation:
- [ ] Upload project to PyPi for easy installation with pip.
- [ ] HTML and CSS customization options.
- [ ] Use [goo.gl](https://goo.gl) to shorten URLs.


## See Also
- [Udacity's Nanodegrees](https://www.udacity.com/nanodegree)
- [webbrowser - Convenient Web-browser controller](https://docs.python.org/3.7/library/webbrowser.html#module-webbrowser)
- [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/user/install/)

## Footnotes

1. <a id="footnote-1"></a>
   [Python Data Structures - Dictionaries](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries)
2. <a id="footnote-2"></a>
   [Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
3. <a id="footnote-3"><a/>
   [Google API Client Library for Python](https://developers.google.com/api-client-library/python/start/get_started)
4. <a id="footnote-4"><a/>
   [Open Movie Database API documentation](http://www.omdbapi.com)

[str]: https://docs.python.org/2/library/stdtypes.html#typesseq
[dict]: https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries
[list]: https://docs.python.org/2.7/tutorial/datastructures.html

## Licence

MIT License

Copyright (c) 2017 Kevin W. Lazich

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
