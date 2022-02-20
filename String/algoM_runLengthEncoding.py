# https://www.algoexpert.io/questions/Run-Length%20Encoding
# O(n) time, O(n) space


def runLengthEncoding(string):
    # Write your code here.
    count = 0
    res = ""

    for char in string:
        if count == 0:
            ele = char
            count += 1
        elif char == ele and count < 9:
            count += 1
        else:
            res += (str(count) + ele)
            ele = char
            count = 1

    res += (str(count) + ele)
    return res
