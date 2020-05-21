import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        dict = {}
        res = []
        for item in (A+" "+B).split(" "):
            if item not in dict.keys():
                dict[item] = 1
            else:
                dict[item]+=1
        for key in dict.keys():
            if dict[key] == 1:
                res.append(key)
        return res
print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))