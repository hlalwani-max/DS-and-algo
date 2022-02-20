class Solution:
    def sort_wods(self, str):
        words = [w.lower()+w for w in str.split()]
        # print(list.sort())
        return ' '.join(w[len(w)//2:] for w in sorted(words))


res = Solution().sort_wods("hi you You are awesome")
print(res)