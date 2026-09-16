



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


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

