from collections import Counter


def favoriteVideoGenre(numUsers, userBooksListenedTo, numGenres, bookGenres):
    # WRITE YOUR CODE HERE
    result = {}
    bookToGenre = {}
    for key in bookGenres:
        for val in bookGenres[key]:
            bookToGenre[val] = key
            # if val not in bookToGenre.keys():
            #     bookToGenre[val] = key

    # print(bookToGenre)

    for user in userBooksListenedTo:
        userGenre = [bookToGenre[songs] for songs in userBooksListenedTo[user]]
        mostCommonGenre = []
        counter = Counter(userGenre)
        prev_frequency = -1
        for genre, num in counter.most_common():
            if prev_frequency == -1:
                mostCommonGenre.append(genre)
                prev_frequency = num
            else:
                if num == prev_frequency:
                    mostCommonGenre.append(genre)
        result[user] = mostCommonGenre
    return result


# book to genre one to many mapping
def favoriteVideoGenre_wo_collection(numUsers, userBooksListenedTo, numGenres, bookGenres):
    res = {}
    flip_bookGenre = {}
    # print(bookGenres)

    for genre in bookGenres.keys():
        for book in bookGenres[genre]:
            if book not in flip_bookGenre.keys():
                flip_bookGenre[book] = [genre]
            else:
                flip_bookGenre[book].append(genre)

    # print(flip_bookGenre)

    for user in userBooksListenedTo.keys():
        userGenres = []
        for book in userBooksListenedTo[user]:
            if book in flip_bookGenre.keys():
                for genres in flip_bookGenre[book]:
                    userGenres.append(genres)

        if len(userGenres) == 0:
            res[user] = []
            continue

        count = {}
        for genre in userGenres:
            if genre not in count:
                count[genre] = 1
            else:
                count[genre] += 1
        # print(count)

        max = -1
        for genre, cou in count.items():
            if cou > max:
                max = cou

        # print(max)

        for genre, cou in count.items():
            if cou == max:
                if user not in res:
                    res[user] = [genre]
                else:
                    res[user].append(genre)
    return res


userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"],
    "Harsh": ["sadas"]
}

songGenres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9", "song2"]
}

output = favoriteVideoGenre_wo_collection(2, userSongs, 5, songGenres)
print(output)
