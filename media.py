class Movie():
    """
    Movie Class docstrings
    author : Deya NeMO
    date : 01-06-2017
    twitter : @deyanem0
    This module demonstrates documentation as
    specified by the `Google Python Style guide'
    Examples :
    #import the module to your working file
    import media
    #create an instance of the Movie() class :
    movie_example1 = media.Movie("Movie Name" ,
                                 "Movie Story " ,
                                 "Movie Image" ,
                                 "Movie Trailer")
    # Note when adding the movie trailer please supicfy an external url such
        as youtube , viemo etc....

    """
    def __init__(self, movie_name,
                 movie_story,
                 movie_image,
                 movie_trailer):
        self.movie_name = movie_name
        self.movie_story = movie_story
        self.movie_image = movie_image
        self.movie_trailer = movie_trailer
        print("Movie init Started")
