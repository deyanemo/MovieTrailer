class Movie():
    """
    This class is a movie Class
    author : Deya NeMO
    date : 01-06-2017
    twitter : @deyanem0
    PeAcE
    """
    def __init__(self,movie_name,
                 movie_story,
                 movie_image,
                 movie_trailer):
        self.movie_name            = movie_name
        self.movie_story            = movie_story
        self.movie_image           = movie_image
        self.movie_trailer           = movie_trailer
        print("Movie init Started")
