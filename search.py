"""A valid YouTube.com and omdbapi.com API key are needed for the public 
functions in this module to work. For information on obtaining an API key 
for these services, follow the links bellow.

    - YouTube API key: https://developers.google.com/youtube/v3/getting-started
    - OMDB API key: http://www.omdbapi.com
"""
import requests
from googleapiclient.discovery import build

# We are using api keys saved in a config.py file. This is just to simulate
# obfuscation of sensitive data. In production we want to limit access to API
# keys.
YOUTUBE_API_KEY = ''
OMDB_API_KEY = ''


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
    lowered_dictionary = dict()
    for key in dictionary:
        value = dictionary[key]
        lowered_dictionary[str(key.lower())] = str(value)
    return lowered_dictionary


def youtube_video_id(title, *args):
    """Builds the YouTube service object  and makes tailored API calls.

    Using the Google API client Python library and a valid YouTube API key,
    this function can make tailored api calls to search for movie trailers.

    Using the built service object this function makes API calls specific
    to movie trailers (see the `payload` variable below).

    Args:
        title (str): The movie title to search for
        *args (str or None): Additional words to add to query.
            Such as the movie's release year.
    Returns:
        str: The YouTube video ID linked to the top search result.

    Notes:
        payload (dict): The payload variable holds the query and other
        criteria for the API call.
            - `q` - The query string using 'trailer' along with the passed
                    movie title and any additional terms.
            - `part` - Specifies the type of resource the API response
                       will include. In this case `id`.
            - `maxResults` - The max count of hits to include in response.
            - `type` - The resource type to retrieve from.
            - `topicId` - Restricts search to specific topics (`/m/02vxn`
                          is the Movie topic ID).
    References:
        - https://developers.google.com/youtube/v3/docs/search/list
        - https://developers.google.com/api-client-library/python
    """

    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    query = '+'.join(
        ['trailer', title] + [x for x in args if x is not None])

    payload = dict(q=query,
                   part="id",
                   maxResults=1,
                   type='video',
                   topicId='/m/02vxn')

    # Call the search.list method to retrieve results matching the
    # specified query term.
    search = youtube.search().list(**payload)
    response = search.execute()

    video_id = response['items'][0]['id']['videoId']  # we just need the ID

    return str(video_id)


def omdb_movie_info(title, year=None):
    """Places GET calls to omdbapi.com using the Python requests pkg.

    This function creates a request payload given a valid OMDB API key and
    using the requests library, places a GET request to omdbapi.com.

    Args:
        title (str): The movie title.
        year (str or None): the movie's release year.
    Returns:
        dict: The request response JSON as a dictionary.

    Notes:
        `type`, `t` and `y` are OMDB API parameters: type of result to
        return, Title and Year.
    References:
        - http://www.omdbapi.com/
        - http://docs.python-requests.org/en/master/
    """
    omdb_url = 'http://www.omdbapi.com/'

    # See omdbapi.com for details on query parameters.
    payload = dict(apikey=OMDB_API_KEY,
                   type='movie',
                   t=title,
                   y=year)

    # place HTTP GET request using the Python requests package.
    response = requests.get(omdb_url, params=payload)
    response.raise_for_status()

    return _lower_keys(response.json())
