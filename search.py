"""A valid YouTube.com and omdbapi.com API key are needed for the public 
functions in this module to work. For information on obtaining an API key 
for these services, follow the links bellow.

    - YouTube API key: https://developers.google.com/youtube/v3/getting-started
    - OMDB API key: http://www.omdbapi.com
"""
import requests
from googleapiclient.discovery import build


def _lower_keys(dictionary):
    """Helper. Converts all keys in a dictionary to lowercase.

    Used in omdb_search to convert the keys in the API response dictionary to 
    lowercase before the function returns. The keys in a response from a 
    request to omdbapi.com are all in title-case and that just isn't cool man. 

    Args:
        dictionary (dict): A dictionary
    Returns:
        dict: The dictionary with all keys now lowercase.
    """
    lowered_dictionary = {}
    for key, value in dictionary.iteritems():
        lowered_dictionary[str(key.lower())] = str(value)
    return lowered_dictionary


def youtube_search(dev_key):
    """Builds the YouTube service object and returns a function to use it.

    Using the Google API client Python library and a valid YouTube API key, 
    this function returns a function that can make tailored api calls to 
    search for movie trailers.

    Args:
        dev_key (str): A valid YouTube API key needed to make requests to 
            the YouTube API. 
    Returns:
        object(): A function that makes specific calls to to the YouTube 
        service object.

    References:
        - https://developers.google.com/api-client-library/python
    """
    youtube = build('youtube', 'v3', developerKey=dev_key)

    def youtube_video_id_requester(title, *args):
        """Makes tailored API calls to YouTube using the built service obj.

        Using the built service object this function makes API calls specific 
        to movie trailers (see the `payload` variable below).

        Args:
            title (str): The movie title to search for
            *args (str|None): Additional words to add to query. 
                Such as the movie's release year.
        Returns:
            str: The YouTube video ID linked to the top search result.

        References:
            - https://developers.google.com/youtube/v3/docs/search/list
        Notes:
            payload (dict): The payload variable holds the query and other 
            criteria for the API call.
                
            q -- The query string using 'trailer' along with the passed 
            movie title and any additional terms. 
            part -- Specifies the type of resource the API response will 
            include. In this case `id`.
            maxResults -- The max count of hits to include in response.
            type -- The resource type to retrieve from. 
            topicId -- Restricts search to specific topics (`/m/02vxn` is 
            the Movie topic ID).
        """
        query = '+'.join(
            ['trailer', title] + [x for x in args if x is not None])

        payload = {'q': query,
                   'part': "id",
                   'maxResults': 1,
                   'type': 'video',
                   'topicId': '/m/02vxn'}
        # Call the search.list method to retrieve results matching the
        # specified query term.
        search = youtube.search().list(**payload)
        response = search.execute()

        video_id = response['items'][0]['id']['videoId']  # just need the ID

        return str(video_id)

    return youtube_video_id_requester


def omdb_search(dev_key):
    """Initialises a request payload and returns a function to use it.

    This function creates a request payload given a valid OMDB API key and 
    returns a function that adds more query parameters to payload and, 
    using the requests library, places a GET request to omdbapi.com.

    Args:
        dev_key (str): A valid omdbapi.com API key.
    Returns:
        object(): A function that make specific HTTP GET requests to 
            omdbapi.com.

    References:
        - http://www.omdbapi.com/
        - http://docs.python-requests.org/en/master/
    """
    omdb_url = 'http://www.omdbapi.com/'

    payload = {'apikey': dev_key, 'type': 'movie'}

    def omdb_movie_info_requester(title, year=None):
        """...

        Args:
            title (str): The movie title
            year (str|None): the movie's release year  
        Returns:
            dict: The request response JSON as a dictionary.
        Notes:
            type, t and y are OMDB API parameters meaning type of result to 
            return, Title and Year.
        """
        payload['t'] = title
        payload['y'] = year

        response = requests.get(omdb_url, params=payload)
        response.raise_for_status()

        return _lower_keys(response.json())

    return omdb_movie_info_requester
