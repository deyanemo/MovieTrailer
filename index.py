# importing media Movie classs
import media
# importing the html constructor
import fresh_html
# making movie instance
starWars1 = media.Movie("Star Wars episode 1 ", "a star wars story",
                        "https://upload.wikimedia.org/wikipedia/en/4/40/" +
                        "Star_Wars_Phantom_Menace_poster.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")
# star wars 2
starWars2 = media.Movie("Star Wars episode 2", "a star wars story",
                        "https://images-na.ssl-images-amazon.com/images/" +
                        "I/51BGV8AJ4RL.jpg",
                        "https://www.youtube.com/watch?v=CO2OLQ2kiq8")
# star wars 3
starWars3 = media.Movie("Star Wars episode 3", "a star wars story",
                        "https://s-media-cache-ak0.pinimg.com/736x/d0/52/ee/" +
                        "d052eec806868a6122179c953baaed6d.jpg",
                        "https://www.youtube.com/watch?v=5UnjrG_N8hU")
# star wars 4
starWars4 = media.Movie("Star Wars episode 4", "a star wars story",
                        "https://i.jeded.com/i/star-wars-episode-iv--a-" +
                        "new-hope.12987.jpg",
                        "https://www.youtube.com/watch?v=9gvqpFbRKtQ")
# star wars 5
starWars5 = media.Movie("Star Wars episode 5", "a star wars story",
                        "http://img5.hostingpics.net/pics/855102Star_Wars_" +
                        "L_empire_contre_attaque.jpg",
                        "https://www.youtube.com/watch?v=JNwNXF9Y6kY")
# star wars 6
starWars6 = media.Movie("Star Wars episode 6", "a star wars story",
                        "https://images-na.ssl-images-amazon.com/images/I/" +
                        "51ELRnj3VnL._SY445_.jpg",
                        "https://www.youtube.com/watch?v=MYD_xxY5wEI")
# star wars 7
starWars7 = media.Movie("Star Wars episode 7", "a star wars story",
                        "https://s-media-cache-ak0.pinimg.com/originals/91" +
                        "/69/eb/9169eb0d958c5ea2ed1c9eac3d6b1efa.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")
# star wars 8
starWars8 = media.Movie("Star Wars episode 8 ", "a star wars story",
                        "https://www.flickeringmyth.com/wp-content/uploads/" +
                        "2017/02/16806837_712489342244455_67670754037713324" +
                        "63_n-600x890.jpg",
                        "https://www.youtube.com/watch?v=VZSKN312BXw")
# adding all the movies to a single list
movies_to_show = [starWars1, starWars2, starWars3,
                  starWars4, starWars5, starWars6, starWars7, starWars8]

# passing the movies as a list to html function
fresh_html.sss(movies_to_show)
