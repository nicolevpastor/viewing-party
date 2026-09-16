


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

# 2. Create a function named `add_to_watched`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
#     - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watched"` list inside of `user_data`
# - return the `user_data`
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data
    
# 3. Create a function named `add_to_watchlist`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
#     - An empty list represents that the user has no movies in their watchlist
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watchlist"` list inside of `user_data`
# - return the `user_data`

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data



# 4. Create a function named `watch_movie`. This function should...

# - take two parameters: `user_data`, `title`
#   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
#     - This represents that the user has a watchlist and a list of watched movies
#   - the value of `title` will be a string
#     - This represents the title of the movie the user has watched
# - If the title is in a movie in the user's watchlist:
#   - remove that movie from the watchlist
#   - add that movie to watched
#   - return the `user_data`
# - If the title is not a movie in the user's watchlist:
#   - return the `user_data`

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

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
    user_watched_list = user_data['watched']
    friends_watched_list =[]
    friends = user_data['friends']
    for friend in friends:
        for movie in friend['watched']:
            friends_watched_list.append(movie["title"])
    
    unique_movies =[]
    for movie in user_watched_list:
        if movie['title'] not in friends_watched_list:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    user_watched_list = []
    for movie in user_data['watched']:
        user_watched_list.append(movie['title'])

    unique_movies= []
    for friends in user_data['friends']:
        for movie in friends["watched"]:
            if movie['title'] not in user_watched_list:
                if movie['title'] not in [unique_movie['title'] for unique_movie in unique_movies]:
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








