class Solution:
    def reorderLogFiles(logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0,)
            # print(id_,rest)
            # print(log.split(" ", 2))
            return (0, rest, id_) if log[0].isAlpha() else (1,)
        # f(lo)
        return sorted(logs, key=f)
inp = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
print(Solution.reorderLogFiles(inp))