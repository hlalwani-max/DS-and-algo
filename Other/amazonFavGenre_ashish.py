from collections import Counter
def favoriteVideoGenre(numUsers, userBooksListenedTo, numGenres, bookGenres):
    # WRITE YOUR CODE HERE
    result = {}
    bookToGenre = {}
    for genre in bookGenres:
        for book in bookGenres[genre]:
            bookToGenre[book] = genre
    

    for user in userBooksListenedTo:
        user_list = []
        user_genres = [bookToGenre[book] for book in userBooksListenedTo[user]]
        c = Counter(user_genres)
        prev_freq = -1
        # print(c.most_common())
        for item, num in c.most_common():
            if prev_freq < 0:
                user_list.append(item)
                prev_freq = c[item]
            else:
                if c[item] == prev_freq:
                    user_list.append(item)
                else:
                    continue
        result[user] = user_list

    return result

# userSongs = {
#    "David": [],
#    "Emma":  []
# }
#
# songGenres = {
#    "Rock":    [],
#    "Dubstep": [],
#    "Techno":  [],
#    "Pop":     [],
#    "Jazz":    []
# # }
# userSongs = {}
#
# songGenres = {}


userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}

songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

# Output: {
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }

output = favoriteVideoGenre(2,userSongs,5,songGenres)
print(output)