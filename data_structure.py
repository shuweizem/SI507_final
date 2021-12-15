import json
import webbrowser

f = open("movieDictData.json","r")
movieDict = json.loads(f.read())
f.close()

#The structure of the movie tree
tree = ['Please choosing the movie runtime: (1)<=90 min (2)>90 min', \
         ['Please choosing the year of the movie: (1)<=1980 (2)1980~2000 (3)>2000', \
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', \
             [],[],[],[],[],[],[],[],[],[],[]], \
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', \
             [],[],[],[],[],[],[],[],[],[],[]], \
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', \
             [],[],[],[],[],[],[],[],[],[],[]] \
         ], \
         ['Please choosing the year of the movie: (1)<=1980 (2)1980~2000 (3)>2000',\
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', \
             [],[],[],[],[],[],[],[],[],[],[]], \
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', \
             [],[],[],[],[],[],[],[],[],[],[]], \
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', \
             [],[],[],[],[],[],[],[],[],[],[]] \
         ] \
       ]


#sort the movie by different genre, and store the movie in the movie tree
def sortMovieGenre(movie, runtimeSide, yearSide):
    if "Crime" in movie["Genre"]:
        tree[runtimeSide][yearSide][1].append(movie)
    if "Drama" in movie["Genre"]:
        tree[runtimeSide][yearSide][2].append(movie)
    if "Comedy" in movie["Genre"]:
        tree[runtimeSide][yearSide][3].append(movie)
    if "Horror" in movie["Genre"]:
        tree[runtimeSide][yearSide][4].append(movie)
    if "Action" in movie["Genre"]:
        tree[runtimeSide][yearSide][5].append(movie)
    if "Sci-Fi" in movie["Genre"]:
        tree[runtimeSide][yearSide][6].append(movie)
    if "Documentary" in movie["Genre"]:
        tree[runtimeSide][yearSide][7].append(movie)
    if "Animation" in movie["Genre"]:
        tree[runtimeSide][yearSide][8].append(movie)
    if "Thriller" in movie["Genre"]:
        tree[runtimeSide][yearSide][9].append(movie)
    if "Adventure" in movie["Genre"]:
        tree[runtimeSide][yearSide][10].append(movie)
    if "Crime" not in movie["Genre"] and "Drama" not in movie["Genre"] and "Comedy" not in movie["Genre"] and \
       "Horror" not in movie["Genre"] and "Action" not in movie["Genre"] and "Sci-Fi" not in movie["Genre"] and \
       "Documentary" not in movie["Genre"] and "Animation" not in movie["Genre"] and "Thriller" not in movie["Genre"] and \
       "Adventure" not in movie["Genre"]:
       tree[runtimeSide][yearSide][11].append(movie)


#sort and store movies
for movie in movieDict:
    runtime = ''.join(filter(lambda i: i.isdigit(), movie["Runtime"]))
    if int(runtime) <= 90:
        if int(movie["Year"][0:4]) <= 1980:
            sortMovieGenre(movie, 1, 1)
        elif 1980 < int(movie["Year"][0:4]) <= 2000:
            sortMovieGenre(movie, 1, 2)
        elif int(movie["Year"][0:4]) > 2000:
            sortMovieGenre(movie, 1, 3)
    else:
        if int(movie["Year"][0:4]) <= 1980:
            sortMovieGenre(movie, 2, 1)
        elif 1980 < int(movie["Year"][0:4]) <= 2000:
            sortMovieGenre(movie, 2, 2)
        elif int(movie["Year"][0:4]) > 2000:
            sortMovieGenre(movie, 2, 3)

with open("tree.json", "w") as outfile:
    json.dump(tree, outfile)
