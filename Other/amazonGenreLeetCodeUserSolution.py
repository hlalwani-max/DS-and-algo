import collections
def favGenres(userSongs, songGenres):
    output = {}
    # print(type(userSongs))
    for i in userSongs.keys():
        # print(userSongs[i])
        # print(i)
        list = userSongs[i]
        count = collections.defaultdict(int)
        for j in list:
            for k, v in songGenres.items():
                if j in v:
                    count[k] += 1

        # print(count)
        output[i] = [key for key, val in count.items() if val == max(count.values())]

    return output

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

output = favGenres(userSongs,songGenres)
print(output)