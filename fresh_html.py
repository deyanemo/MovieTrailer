import webbrowser
import os
import re
import media

body_content = """

<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<head>
<title>Movie Day</title>
<link rel="stylesheet" href="style.css">
</head>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="main.js"></script>
<body>
<div class="container">
<div class="header"><h1>Movie Day</h1></div>
<div class="movies">

"""

footer_content = """
</div>
<footer>
<p>All rights reseved to DEYANEMO (c) 2017 </p>
<p>Twitter : @deyanemo</p>
</footer>
</div>

</body>
</html>
"""

item_content = """

<div class="item">
<img src="https://placeimg.com/200/300/arch" class="movieimg">
<p class="movie_name">Star Wars episode 1</p>
</div>
<div class="model">
<iframe width="100%" height="100%" src="https://www.youtube.com/embed/XGSy3_Czz8k" style="border: none;"></iframe>
<p class="close">X</p>
</div>



"""


# The Function
def sss(movies_list):
    movies_list = movies_list
    # open a file
    f = open("index.html","w+")
    f.write(body_content)
    for i in movies_list:
        f.write("<div class=\"item\">")
        f.write("<a href=\""+i.movie_trailer +" \" target='_blank'>")
        f.write("<img src=\" " + i.movie_image + "\"class=movieimg>")
        f.write("</a>")
        f.write("<p class=movie_name>" + i.movie_name +"</p>")
        f.write("</div>")
        f.write("\n")
    f.write(footer_content)
    f.close()










