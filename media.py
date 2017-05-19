"""

"""
from webbrowser import open as open_url


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
        open_url(self.trailer_youtube_url)
