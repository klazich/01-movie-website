from media import Movie

# Creating an instance by hard-coding in the values:
INCEPTION = Movie('Inception',
                  'A thief, who steals corporate secrets through use ...',
                  'https://www.youtube.com/watch?v=YoHD9XEInc0',
                  'https://images-na.ssl-images-amazon.com/images/M/M...')

# # Creating an instance by first using `get_movie_data to get the values:
# MAD_MAX_DATA = Movie.get_movie_data('Mad Max', '2015')  # passing the year
# MAD_MAX = Movie(MAD_MAX_DATA['title'],
#                 MAD_MAX_DATA['plot'],
#                 MAD_MAX_DATA['youtube_url'],
#                 MAD_MAX_DATA['poster'],
#                 MAD_MAX_DATA)
#
# # Creating an instance in one line using the shortcut `.movie`:
# PRIMER = Movie.movie('Primer')
