def match(prefix, suffix):
    lengthS = len(suffix)
    lengthP = len(prefix)

    if lengthP == 0:
        return lengthP + lengthS
    if lengthS == 0:
        return 0
    if prefix[0] != suffix[0]:
        return 0

    counter = 0
    i, j = 0, 0
    # print(prefix, suffix)

    while j < lengthS:
        if j == lengthS:
            return counter
        if prefix[i] == suffix[j]:
            counter += 1
            i = (i + 1) % lengthP
            j += 1
        else:
            return counter

    return counter


def commonPrefixLength(s):
    length = len(s)
    prefixSum = 0
    for i in range(length):
        prefix = s[:i]
        suffix = s[i:]
        matchVal = match(prefix, suffix)
        prefixSum += matchVal
        # print('{} {} : {}'.format(prefix, suffix, matchVal))

    return prefixSum


def commonPrefix(inputs):
    results = []
    for inp in inputs:
        res = commonPrefixLength(inp)
        results.append(res)

    return results


if __name__ == "__main__":
    # match("ababa", "a")
    _input = ["ababaa", "aa"]
    result = commonPrefix(_input)
    print('Output : {}'.format(result))
