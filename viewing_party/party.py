
#---------HELPER_FUNCTIONS---------
def get_friends_watched_movies(user_data):
    friends_watched_movie_list =[]
    
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movie_list.append(movie)
    return friends_watched_movie_list

def get_movie_titles(movies):
    titles =[]
    for movie in movies:
        titles.append(movie["title"])
    return titles
    

def create_movie(title, genre, rating):

    if title and genre and rating:
        dictionary1 = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return dictionary1
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data
    


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    count = len(user_data['watched'])
    total =0
    if not user_data['watched']:
        return 0.0
    for movie in user_data['watched']:
        total += movie["rating"]
    return float (total /count )


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    #create a frequency map to count genre
    freq_map ={}
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in freq_map:
            freq_map[genre] += 1
        else:
            freq_map[genre] = 1
    # Return mostly watched genre
    max_count = 0
    most_watched = ""
    for genre, count in freq_map.items():
        if count > max_count:
            max_count =count
            most_watched = genre
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_movies = user_data['watched']
    friends_movies = get_friends_watched_movies(user_data)
    movie_titles = get_movie_titles(friends_movies)
    print(movie_titles)
    
    unique_movies =[]
    for movie in user_movies:
        if movie['title'] not in movie_titles:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friends_movies = get_friends_watched_movies(user_data)
    user_movie_titles = get_movie_titles(user_movies)
    
    unique_movies= []
    for movie in friends_movies:
            if movie['title'] not in user_movie_titles:
                if movie['title'] not in get_movie_titles(unique_movies):
                    unique_movies.append(movie)
    return unique_movies
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    recommended_movies = []
    movie_list = get_friends_unique_watched(user_data)


    for movie in movie_list:
        if movie['host'] in user_data['subscriptions']:
            recommended_movies.append(movie)
    return recommended_movies

    print("Movie List: ", movie_list)


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#need friends watched movies from test_constants
#wave 5 has favorites in user_data thats the users
#trying to access favorites in userdata given in test_constants
# we check each movie in favorites and see if it is in friends watched list, if not
#  we add to recommended movies list
def get_new_rec_by_genre(user_data):
    recommeded_movies =[]
    genre = get_most_watched_genre(user_data)
    movies = get_friends_unique_watched(user_data)
    for movie in movies:
        if movie['genre'] == genre:
            recommeded_movies.append(movie)
    return recommeded_movies

def get_rec_from_favorites(user_data):
    recommended_movies =[]
    friends_movies = get_friends_watched_movies(user_data)
    friends_movie_titles = get_movie_titles(friends_movies)
    for movie in user_data['favorites']:
        if movie['title'] not in friends_movie_titles:
            recommended_movies.append(movie)
    return recommended_movies











