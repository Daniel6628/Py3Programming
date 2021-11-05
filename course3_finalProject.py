'''
The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. 
The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites 
(Rotten Tomatoes, IMDB, etc.).
You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of 
related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache.
'''
import requests
import json

def get_movies_from_tastedive(movie_name):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = movie_name
    params_diction["type"] = "movies"
    params_diction["limit"] = 5
    tastedive_resp = requests.get(baseurl, params = params_diction)
    print(tastedive_resp.url)
    return tastedive_resp.json()

similar_movies = get_movies_from_tastedive("Black Panther")
print(similar_movies)

'''
Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of 
movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
'''
#pass the previous function into the following function
def extract_movie_titles(movie_dict = get_movies_from_tastedive):
    title_list = [movie['Name'] for movie in movie_dict['Similar']['Results']]
    return title_list

m_extract = extract_movie_titles(get_movies_from_tastedive("Black Panther"))
print(m_extract)

'''
Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, 
called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for 
all of them, and combines them all into a single list. Don’t include the same movie twice.
'''
import requests
import json

def get_movies_from_tastedive(movie_name):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = movie_name
    params_diction["type"] = "movies"
    params_diction["limit"] = 5
    tastedive_resp = requests.get(baseurl, params = params_diction)
    print(tastedive_resp.url)
    return tastedive_resp.json()

#pass the previous function into the following function
def extract_movie_titles(movie_dict = get_movies_from_tastedive):
    title_list = [movie['Name'] for movie in movie_dict['Similar']['Results']]
    return title_list

def get_related_titles(movie_list):
    movie_collection = []
    for movie in movie_list:
        d = get_movies_from_tastedive(movie)
        lst = extract_movie_titles(d)
        for m in lst:
            if m not in movie_collection:
                movie_collection.append(m)
            else:
                continue
    return movie_collection

x = get_related_titles(["Black Panther", "Captain Marvel"])
print(x)

'''
Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. 
The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. 
You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to 
extract existing data from the cache.
'''
import requests
import json

def get_movie_data(m_title):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction["apikey"] =  "e702077c"
    params_diction["t"] = m_title
    params_diction["r"] = "json"
    omdb_resp = requests.get(baseurl, params_diction)
    print(omdb_resp.url)
    return omdb_resp.json()

m_info_d = get_movie_data("Black Panther")
'''
Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. 
It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary 
for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
'''
import requests
import json

def get_movie_data(m_title):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction["apikey"] =  "e702077c"
    params_diction["t"] = m_title
    params_diction["r"] = "json"
    omdb_resp = requests.get(baseurl, params_diction)
    print(omdb_resp.url)
    return omdb_resp.json()

m_info_d = get_movie_data("Black Panther")
print(type(m_info_d))
#print(json.dumps(m_info_d, indent = 2))

def get_movie_rating(d = get_movie_data):  
    tomato_rating = d["Ratings"][1]["Value"]
    rating_type = d["Ratings"][1]["Source"]
    if rating_type == "Rotten Tomatoes" and tomato_rating != "N/A":
        return int(tomato_rating.strip('%'))
    else:
         return 0

r = get_movie_rating(m_info_d)
print(r)

'''
Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. 
Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as 
output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, 
as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
'''
import requests
import json

def get_movies_from_tastedive(movie_name):
    baseurl = "https://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = movie_name
    params_diction["type"] = "movies"
    params_diction["limit"] = 5
    tastedive_resp = requests.get(baseurl, params = params_diction)
    #print(tastedive_resp.url)
    return tastedive_resp.json()

#pass the previous function into the following function
def extract_movie_titles(movie_dict = get_movies_from_tastedive):
    title_list = [movie['Name'] for movie in movie_dict['Similar']['Results']]
    return title_list

def get_related_titles(movie_list):
    movie_collection = []
    for movie in movie_list:
        d = get_movies_from_tastedive(movie)
        lst = extract_movie_titles(d)
        for m in lst:
            if m not in movie_collection:
                movie_collection.append(m)
            else:
                continue
    return movie_collection

def get_movie_data(m_title):
    baseurl = "http://www.omdbapi.com/"
    params_diction = {}
    params_diction["apikey"] =  "e702077c"
    params_diction["t"] = m_title
    params_diction["r"] = "json"
    omdb_resp = requests.get(baseurl, params_diction)
    #print(omdb_resp.url)
    return omdb_resp.json()

def get_movie_rating(d = get_movie_data):  
    tomato_rating = d["Ratings"][1]["Value"]
    rating_type = d["Ratings"][1]["Source"]
    if rating_type == "Rotten Tomatoes" and tomato_rating != "N/A":
        return int(tomato_rating.strip('%'))
    else:
         return 0
        
def get_sorted_recommendations(movie_title_list):
    ratings_tup_lst = []
    ratings_lst = []
    related_title_list = get_related_titles(movie_title_list)
    for movie in related_title_list:
        dic = get_movie_data(movie)
        ratings = get_movie_rating(dic)
        ratings_tup_lst.append((ratings, movie))
    result = sorted(ratings_tup_lst, key = lambda x: (x[0], x[1]) ,reverse = True)
    for i in result:
        ratings_lst.append(i[1])
        
    return ratings_lst
#test:
m = get_sorted_recommendations(["Black Panther", "Captain Marvel", "Venom"])
print(m)

'''
OR even better version of the last function: get_sorted_recommendations()
'''
def get_sorted_recommendations(movie_title_list):
    ratings_dict = {}
    related_title_list = get_related_titles(movie_title_list)
    
    for movie in related_title_list[:5]:
        ratings = get_movie_rating(get_movie_data(movie))
        ratings_dict[movie] = ratings

    return [movie[0] for movie in sorted(ratings_dict.items(), key = lambda x: (x[1], x[0]), reverse = True)]
