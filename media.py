import webbrowser
import search
import config

# For constructing a youtube link from a youtube video ID.
YOUTUBE_URL = 'https://www.youtube.com/watch?v={}'

get_youtube_id = search.youtube_search(config.YOUTUBE_API_KEY)
get_omdb_movie_info = search.omdb_search(config.OMDB_API_KEY)


class Movie:
    """A class for encapsulating a movie's information
    
    Creates Movie entities that are used by fresh_tomatoes.py in rendering 
    the website's HTML. 
    """

    # def __init__(self, title, storyline, youtube_url, image_url,
    #              release_year=None, movie_info=None):

    def __init__(self, title,  **kwargs):
        """Constructor for Movie class.
        
        Sets Movie instance attributes.
        
        Args:
            title (str): The title of the movie.
            storyline (str|None): The plot/storyline of the movie.
            youtube_url (str|None): A URL pointing to a                 
                youtube.com video of a trailer of the movie.
            image_url (str|None): A URL pointing to an image of the movie 
                poster or box art.
            release_year (str|None): The year the move was 
                released in theater.
            movie_info(dict|None): An optional dictionary of 
                additional movie information.
        """
        self.title = title
        self.year = kwargs.get('year', None)
        self.storyline = kwargs.get('plot', None)
        self.trailer_youtube_url = kwargs.get('trailer_youtube_url', None)
        self.trailer_youtube_id = kwargs.get('trailer_youtube_id', None)
        self.poster_image_url = kwargs.get('poster', None)
        self.info = kwargs

    def show_trailer(self):
        """Opens trailer_youtube_url in default web browser."""
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        """Opens the poster_image_url in default web browser."""
        webbrowser.open(self.poster_image_url)

    @staticmethod
    def get_movie_metadata(movie_title, year=None, *queries):
        """Fetch data on movie using omdbapi and youtube API.

        Using the functions from search.py this static function returns a 
        dictionary of the metadata.

        Args:
            movie_title (str): The movie title.
            year (str|None): The movie's release year.
            *queries (str): Additional query terms.
        Returns:
            dict: A dictionary of compiled movie info.
        """
        movie_info = get_omdb_movie_info(movie_title, year)
        video_id = get_youtube_id(movie_title, year, *queries)

        metadata = movie_info
        # Add youtube data to dictionary
        metadata['trailer_youtube_id'] = video_id
        metadata['trailer_youtube_url'] = YOUTUBE_URL.format(video_id)

        return metadata
