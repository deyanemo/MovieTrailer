import media
import fresh_html
starWars1 = media.Movie("Star Wars","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","https://www.youtube.com/watch?v=1g3_CFmnU7k")
starWars2 = media.Movie("The Empire Strikes Back","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","https://www.youtube.com/watch?v=1g3_CFmnU7k")
starWars3 = media.Movie("Return of the Jedi","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","https://www.youtube.com/watch?v=1g3_CFmnU7k")
starWars4 = media.Movie("Star wars episode I","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","https://www.youtube.com/watch?v=1g3_CFmnU7k")
starWars5 = media.Movie("star wars episode II","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","https://www.youtube.com/watch?v=1g3_CFmnU7k")
starWars6 = media.Movie("star wars episode III","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","https://www.youtube.com/watch?v=1g3_CFmnU7k")
starWars7 = media.Movie("star wars episode IIII","a star wars story","http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX","trailer")

movies_to_show = [starWars1,starWars2,starWars3,starWars4,starWars5,starWars6,starWars7]

fresh_html.sss(movies_to_show)
