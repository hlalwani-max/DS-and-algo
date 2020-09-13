# Math- https://www.interviewbit.com/problems/sorted-permutation-rank/
# Video explanation- https://www.youtube.com/watch?v=gqlSxpOegoY
import math


class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        lA = len(A)
        ans = 0
        bool = [1] * lA
        sortedA = sorted(A)

        i = 0
        j = 0
        while i < lA and j < lA:
            if bool[j] == 0:
                j += 1
                continue
            elif A[i] != sortedA[j]:
                ans += math.factorial(lA - i - 1)
            else:
                bool[j] = 0
                i += 1
                j = -1

            j += 1

        return (ans + 1) % 1000003


inp = "acb"
out = Solution().findRank(inp)
print(out)
