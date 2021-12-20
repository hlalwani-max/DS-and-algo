# TC- O(n) - n competitions SC- O(c) - c unique teams
def tournamentWinner(competitions, results):
    dict = {}

    # giving points to winner (in dictionary)
    for i in range(len(competitions)):
        home, away = competitions[i][0], competitions[i][1]
        if results[i] == 1:
            if home not in dict:
                dict[home] = 3
            else:
                dict[home] += 3
        else:
            if away not in dict:
                dict[away] = 3
            else:
                dict[away] += 3

    # finding winner by finding maximum of dictionary values
    winner_score = 0
    winner = ""
    for key in dict.keys():
        if dict[key] > winner_score:
            winner = key
            winner_score = dict[key]

    return winner
