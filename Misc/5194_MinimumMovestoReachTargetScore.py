class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        minMoves = 0
        while target > 1:
            if target % 2 != 0:
                target -= 1
                minMoves += 1
            else:
                if maxDoubles > 0:
                    target = int(target / 2)
                    maxDoubles -= 1
                    minMoves += 1
                else:
                    diff = target - 1
                    target -= diff
                    minMoves += diff

        return minMoves


inp = [19,
       2]
print(Solution().minMoves(inp[0], inp[1]))
