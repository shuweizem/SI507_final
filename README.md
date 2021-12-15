# How to supply API Keys
- Apply an API Key at OMDb API. (Link: http://www.omdbapi.com/apikey.aspx)
- Fill your API Key into the fetch_data.py. (key = "your-api-key”)

# Required Package
- requests
- webbrowser

# Data Structure
- Create a tree to store the data. The data structure is like:
```
tree = ['Please choosing the movie runtime: (1)<=90 min (2)>90 min', 
           ['Please choosing the year of the movie: (1)<=1980 (2)1980~2000 (3)>2000', 
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', 
             [],[],[],[],[],[],[],[],[],[],[]], 
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', 
             [],[],[],[],[],[],[],[],[],[],[]], 
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', 
             [],[],[],[],[],[],[],[],[],[],[]] 
         ], 
           ['Please choosing the year of the movie: (1)<=1980 (2)1980~2000 (3)>2000',
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', 
             [],[],[],[],[],[],[],[],[],[],[]], 
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', 
             [],[],[],[],[],[],[],[],[],[],[]], 
           ['Please choosing the genre of the movie: (1)Crime (2)Drama (3)Comedy (4)Horror (5)Action (6)Sci-Fi (7)Documentary (8)Animation (9)Thriller (10)Adventure (11)Other', 
             [],[],[],[],[],[],[],[],[],[],[]] 
         ] 
       ]

```

# Interaction
- Run find_movie.py in the command window.
- First, the program will ask the user to choose between the movie runtimes: (1)<=90 min (2)>90 min.
- Second, the program will ask the user to choose movie from desired years: (1)<=1980 (2)1980~2000 (3)>2000.
- Third, the program will prompt  a list of movie genres for the user to choose from, such as Crime, Drama, Comedy etc.
- Once the user made all the choices, the program will provide a list of 10 movies(if there is less than 10 movies, list all the movie)ranked by their IMDB ratings and indexed by number from 1 to 10. 
- User can then type the number before the movie to see the plot , rated and the poster link of the movie, and the program will also automatically use the web browser module to open the posterURL embedded by the JSON item description.

