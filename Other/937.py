class Solution:
    def reorderLogFiles(logs):
        res = []
        digit_res = []
        map = {}
        for item in logs:
            # print(map)
            words = item.split( " ")
            flag = False
            for i in range(1, len(words)):
                if words[i].isdigit():
                    flag = True
            map[item] = flag
        # print(map)
        for item in logs:
            if map[item] is False:
                res.append(item)
        for item in logs:
            if map[item] is True:
                digit_res.append(item)
        # res = sorted(res, key = lambda x: x.split(" ")[1:][0])
        return sorted(res, key = lambda x: x.split(" ")[1:][0]) + digit_res

inp = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
print(Solution.reorderLogFiles(inp))