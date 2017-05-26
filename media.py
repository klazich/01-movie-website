import webbrowser
import search
import config

# For constructing a youtube link from a youtube video ID.
YOUTUBE_URL = 'https://www.youtube.com/watch?v={}'

get_youtube_id = search.youtube_search(config.YOUTUBE_API_KEY)
get_omdb_movie_info = search.omdb_search(config.OMDB_API_KEY)


class Movie:
    """A class for encapsulating a movie's information
    
    Creates `Movie` instances that are used by fresh_tomatoes.py in rendering 
    the website's HTML. 
    """

    def __init__(self, title, plot, youtube_url, image_url,
                 movie_data=None):
        """Constructor for `Movie` class.
        
        Sets `Movie` instance attributes. 
        
        Keyword Args:
            title (str): The title of the movie.
            plot (str): The plot of the movie.
            youtube_url (str): A URL pointing to a youtube.com video of a 
                trailer of the movie.
            image_url (str): A URL pointing to an image of the movie poster 
                or box art.
            movie_data(dict|None): An optional dictionary of 
                additional movie information.
        """
        self.title = title
        self.plot = plot
        self.trailer_youtube_url = youtube_url
        self.poster_image_url = image_url
        self.info = movie_data

    def show_trailer(self):
        """Opens trailer_youtube_url in default web browser."""
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        """Opens the poster_image_url in default web browser."""
        webbrowser.open(self.poster_image_url)

    @staticmethod
    def movie(movie_title, year=None):
        """Shortcut to creating a `Movie` instance with data from 
        `get_movie_data`.
        
        This creates a `Movie` instance by using `get_movie_data` to get the 
        movie information needed.
        
        Args:
            movie_title (str): The movie title.
            year (): The movie's release year
        Returns:
            Movie: A new `Movie` instance.
            
        Examples:
            >>> # Creating a `Movie` instance for the movie Arrival using 
            >>> # `get_movie_data` to first get the values:
            >>> data = Movie.get_movie_data('Arrival')
            >>> arrival = Movie(data['title'],
            ...                 data['plot'],
            ...                 data['youtube_url'],
            ...                 data['poster'])
            
            >>> # The following code does the same as the code above:
            >>> arrival = Movie.movie('Arrival')
        """
        movie_data = Movie.get_movie_data(movie_title, year)

        title = movie_title
        plot = movie_data['plot']
        youtube_url = movie_data['youtube_url']
        image_url = movie_data['poster']

        return Movie(title, plot, youtube_url, image_url, movie_data)

    @staticmethod
    def get_movie_data(movie_title, year=None, *queries):
        """Fetch data on movie using omdbapi and youtube API.

        Using the functions from search.py this static function returns a 
        dictionary of the data.

        Args:
            movie_title (str): The movie title.
            year (str|None): The movie's release year.
            *queries (str): Additional query terms.
        Returns:
            dict: A dictionary of compiled movie info.
        """
        movie_info = get_omdb_movie_info(movie_title, year)
        video_id = get_youtube_id(movie_title, year, *queries)

        data = movie_info
        # Add youtube data to dictionary
        data['youtube_id'] = video_id
        data['youtube_url'] = YOUTUBE_URL.format(video_id)

        return data

