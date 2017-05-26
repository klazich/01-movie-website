#!/usr/bin//python

from media import Movie
from fresh_tomatoes import open_movies_page

INCEPTION = Movie.movie('Inception')
BLADE_RUNNER = Movie.movie('Blade Runner', '1982')
PRIMER = Movie.movie('Primer')
MAD_MAX = Movie.movie('Mad Max', '2015')
SNATCH = Movie.movie('Snatch')
BRICK = Movie.movie('Brick')

MOVIES = [INCEPTION, PRIMER, SNATCH, MAD_MAX, BLADE_RUNNER, BRICK]

open_movies_page(MOVIES)  # Generate HTML and open in browser
