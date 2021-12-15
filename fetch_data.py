import requests
import json

#fetch data from the website
movie_dict = []
movie_count = 0

def get_movie(url,id, ty = "movie" ,key = "your-api-key"): #Enter the key here
    parameter={'i':id , 'type':ty , 'apikey' : key}
    resp = requests.get(url, parameter).json()
    return resp

BASE_URL = "http://www.omdbapi.com"

for i in range(465267, 466268): #movie IMDb ID
    movie_id = "tt0"+str(i)
    data = get_movie(BASE_URL, movie_id)

    if("Year" in data):
        if("Runtime" in data):
            if("Genre" in data):
                if(data["Year"] != "N/A" and data["Runtime"] != "N/A" and data["Genre"] != "N/A" and data["imdbRating"] != "N/A"):
                    #if(int(data["Year"][0:4]) > 1980):
                        movie_dict.append(data)
                        movie_count += 1



print("****************")
print("movie_count: ", movie_count)

with open("movieDictAllNew.json", "w") as outfile:
    json.dump(movie_dict, outfile)

#combine all json file to one
'''
dict_all = []
with open('movieDict1981.json') as f:
    data1 = json.load(f)

with open('movieDictAllNew.json') as f:
    data2 = json.load(f)

dict_all = dict_all + data1 + data2

with open("movieDictData.json", "w") as outfile:
    json.dump(dict_all, outfile)
'''


#check if all the data is stored
'''
i = 0
with open('movieDictData.json') as f:
    m = json.load(f)

for item in m:
    i += 1

print(i)
'''
