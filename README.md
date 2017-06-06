# MovieTrailer
Project for full stack devloper
# please note that main python file is : index.py
    Movie Class docstrings
    author : Deya NeMO
    date : 01-06-2017
    twitter : @deyanem0
    This module demonstrates documentation as specified by the `Google Python Style guide'
    Examples :
    #import the module to your working file
    import media
    # importing the html constructor
    import fresh_html
    #create an instance of the Movie() class :
    movie_example1 = media.Movie("Movie Name","Movie Story ", "Movie Image", " Movie Trailer")
    # Note when adding the movie trailer please supicfy an external url such
        as youtube , viemo etc....
    #now adding a movie to the project
    # making movie instance
    #add as long as you want!
    movie1 = media.Movie("Star Wars", "a star wars story",
                        "http://t3.gstatic.com/images",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")
    movie2 = media.Movie("Star Wars", "a star wars story",
                        "http://t3.gstatic.com/images",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")
    #to create the html file use the following :
    #note that the sss function expect a list
    movies_to_show = [movie1 ,movie2]
    fresh_html.sss(list)