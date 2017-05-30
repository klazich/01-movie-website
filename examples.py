import config
import search
from media import Movie

# Applying API keys
search.YOUTUBE_API_KEY = config.YOUTUBE_API_KEY
search.OMDB_API_KEY = config.OMDB_API_KEY


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Creating a Movie instance with Movie constructor __init__
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

INCEPTION = Movie('Inception',
                  'A thief, who steals corporate secrets through use of'
                  ' dream-sharing technology, is given the inverse task of'
                  ' planting an idea into the mind of a CEO.',
                  'https://www.youtube.com/watch?v=YoHD9XEInc0',
                  'https://goo.gl/NK7fvQ')

print(INCEPTION.title)
# | Inception
print(INCEPTION.plot)
# | A thief, who steals corporate secrets through use of dream-sharing
# |  technology, is given the inverse task of planting an idea into the
# |  mind of a CEO.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Creating an instance by first using `Movie.get_movie_data` to get the values
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

MAD_MAX_DATA = Movie.get_movie_data('Mad Max', '2015')  # passing the year
MAD_MAX = Movie(MAD_MAX_DATA['title'],
                MAD_MAX_DATA['plot'],
                MAD_MAX_DATA['youtube_url'],
                MAD_MAX_DATA['poster'],
                MAD_MAX_DATA)  # pass in the dict for the optional `info` attr.

print(MAD_MAX.title)
# | Mad Max: Fury Road
print(MAD_MAX.plot)
# | A woman rebels against a tyrannical ruler in postapocalyptic Australia in
# |  search for her home-land with the help of a group of female prisoners,
# |  a psychotic worshipper, and a drifter named Max.
for key in MAD_MAX.info:
    entry = '{0:>15} -- {1}'.format(key, MAD_MAX.info[key])
    print(entry)
"""
      boxoffice -- $129,483,877
           year -- 2015
     imdbrating -- 8.1
           plot -- A woman rebels against a tyrannical ruler in postapocalyptic 
                   Australia in search for her home-land with the help of a 
                   group of female prisoners, a psychotic worshipper, and a 
                   drifter named Max.
          rated -- R
          title -- Mad Max: Fury Road
         imdbid -- tt1392190
         writer -- George Miller, Brendan McCarthy, Nick Lathouris
     production -- Warner Bros.
         actors -- Tom Hardy, Charlize Theron, Nicholas Hoult, Hugh Keays-Byrne
           type -- movie
        website -- http://www.madmaxmovie.com/
        ratings -- [{u'Source': u'Internet Movie Database', 
                      u'Value': u'8.1/10'}, 
                    {u'Source': u'Rotten Tomatoes', 
                      u'Value': u'97%'}, 
                    {u'Source': u'Metacritic', 
                      u'Value': u'90/100'}]
         poster -- https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE
                   0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SX300.jpg
     youtube_id -- b_4nzm9ICuo
       director -- George Miller
       released -- 15 May 2015
         awards -- Won 6 Oscars. Another 228 wins & 208 nominations.
      metascore -- 90
          genre -- Action, Adventure, Sci-Fi
    youtube_url -- https://www.youtube.com/watch?v=b_4nzm9ICuo
       response -- True
       language -- English, Russian
            dvd -- N/A
        country -- Australia, USA
        runtime -- 120 min
      imdbvotes -- 631,885
"""


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Creating an instance in one line using the shortcut `Movie.movie`
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

BLADE_RUNNER = Movie.movie('Blade Runner', '1982')  # `year` is optional

print(BLADE_RUNNER.title)
# | Blade Runner
print(BLADE_RUNNER.plot)
# | A blade runner must pursue and try to terminate four replicants who stole
# |  a ship in space and have returned to Earth to find their creator.
for key in BLADE_RUNNER.info:
    entry = '{0:>15} -- {1}'.format(key, BLADE_RUNNER.info[key])
    print(entry)
"""
      boxoffice -- N/A
           year -- 1982
     imdbrating -- 8.2
           plot -- A blade runner must pursue and try to terminate four 
                   replicants who stole a ship in space and have returned to 
                   Earth to find their creator.
          rated -- R
          title -- Blade Runner
         imdbid -- tt0083658
         writer -- Hampton Fancher (screenplay), 
                   David Webb Peoples (screenplay), 
                   Philip K. Dick (novel)
     production -- Warner Bros. Pictures
         actors -- Harrison Ford, Rutger Hauer, Sean Young, Edward James Olmos
           type -- movie
        website -- N/A
        ratings -- [{u'Source': u'Internet Movie Database', 
                      u'Value': u'8.2/10'}, 
                    {u'Source': u'Rotten Tomatoes', 
                      u'Value': u'89%'}, 
                    {u'Source': u'Metacritic', 
                      u'Value': u'89/100'}]
         poster -- https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzMzJ
                   hZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU
                   0OTQ0OTY@._V1_SX300.jpg
     youtube_id -- eogpIG53Cis
       director -- Ridley Scott
       released -- 25 Jun 1982
         awards -- Nominated for 2 Oscars. Another 11 wins & 16 nominations.
      metascore -- 89
          genre -- Sci-Fi, Thriller
    youtube_url -- https://www.youtube.com/watch?v=eogpIG53Cis
       response -- True
       language -- English, German, Cantonese, Japanese, Hungarian
            dvd -- N/A
        country -- USA, Hong Kong, UK
        runtime -- 117 min
      imdbvotes -- 490,977
"""
