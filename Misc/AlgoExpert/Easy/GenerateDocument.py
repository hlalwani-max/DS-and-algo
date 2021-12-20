def generateDocument(characters, document):
    # Write your code here.
    characters_dict = {}
    for item in characters:
        characters_dict[item] = characters_dict[item] + 1 if item in characters_dict else 1

    for item in document:
        if item not in characters_dict:
            return False
        else:
            if characters_dict[item] > 0:
                characters_dict[item] -= 1
            else:
                return False

    return True


input = {
    "characters": "Bste!hetsi ogEAxpelrt x ",
    "document": "AlgoExpert is the Best!"
}

possibility = generateDocument(input["characters"], input["document"])
print(possibility)