# ToDo- shoot youtube video for this problem
# TC - O(N) for N characters in string, SC- O(N)
def firstNonRepeatingCharacter(string):
    char_dict = {}

    #  store frequency of characters in dictionary
    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    # loop through the string to find index of unique character
    for i in range(len(string)):
        if char_dict[string[i]] == 1:
            return i

    return -1


input = {
    "string": "abcdcaf"
}

result = firstNonRepeatingCharacter(input["string"])
print("First non repeating character in this string is at position: {}".format(result))
