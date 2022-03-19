# ------------- WAVE 1 --------------------

from re import U


def create_movie(title, genre, rating):
    if None in [title, genre, rating]:
        return None
    
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    return movie_dict

def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    index = 0
    transfer_movie = False
    watched_list = user_data["watched"]
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if movie["title"] == title:
            transfer_movie = watchlist.pop(index)
            break
        index += 1
    if transfer_movie:
        watched_list.append(transfer_movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    movie_list = user_data["watched"]
    
    for dict in movie_list:
        ratings.append(dict["rating"])
    
    if not ratings:
        return 0.0
    else:
        return sum(ratings) / float(len(ratings))

def get_most_watched_genre(user_data):
    #list of movie dicts
    watched_list = user_data["watched"]
    
    genre_list = []
    for movie in watched_list:
        genre_list.append(movie["genre"])
    
    max_count = max(genre_list, default=None, key=genre_list.count)
    return max_count

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# return list of movie dicts that only the user has watched
def get_unique_watched(user_data):
    # add user's list of watched movies
    user_watched_list = user_data["watched"]

    # each index is a "friend" holding a dictionary
    friends_list = user_data["friends"]
    friends_watched_list = []
    # friend is dictionary of movie lists for each friend (keys: watched, watchlist)
    for friend in friends_list:
        # keep it at one level
        friends_watched_list += friend["watched"]

    unique_list = []
    for movie in user_watched_list:
        if movie not in friends_watched_list:
            unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    unique_list = []

    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in user_watched_list and movie not in unique_list:
                unique_list.append(movie)
    return unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    rec_list = []
    subscription_list = user_data["subscriptions"]
    friends_watched_list = get_friends_unique_watched(user_data)

    for movie in friends_watched_list:
        if movie["host"] in subscription_list:
            rec_list.append(movie)
    return rec_list

#user-data
    #key "subscriptions"
        #list of strings

    # key friends (value is a list)
        #index is dictionary for each friend
            #key - 'watched' is list
                #each index is a movie's dictionary
                    #key "host", for subscribtion service
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)

    if not user_data.get("subscriptions"):
        user_data["subscriptions"] = []

    all_recs_list = get_available_recs(user_data) 
    genre_recs_list = []

    for movie in all_recs_list:
        if movie["genre"] == fav_genre:
            genre_recs_list.append(movie)

    return genre_recs_list
        
def get_rec_from_favorites(user_data):
    # user_data has key "favorites", which is a list of dictionaries
    movie_recs = []
    user_favs = user_data["favorites"]

    #list of dictionaries for each friend
    friends_watched_list = user_data["friends"]
    
    for user_movie in user_favs:
        watched_movie = False
        for friend in friends_watched_list:
            for friend_movie in friend["watched"]:
                if user_movie == friend_movie:
                    watched_movie = True
        if not watched_movie:
            movie_recs.append(user_movie)
    return movie_recs
