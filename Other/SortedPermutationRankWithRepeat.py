from collections import Counter
import math


class Solution:
    def getfactorial(self, n, dic):
        if n == 0 or n == 1:
            return 1
        else:
            ans = 1
            for i in dic.values():
                ans *= math.factorial(i)

            res = (math.factorial(n) // ans) % 1000003
        return res

    # @param A : string
    # @return an integer
    def findRank(self, A):
        lenA = len(A)
        ans = 0
        sortedA = sorted(A)
        bool = [1] * lenA

        i, j = 0, 0
        check = False

        while i < lenA and j < lenA:
            prev = sortedA[j-1] if j > 0 else None
            if bool[j] == 0:
                j += 1
                continue

            if not check and sortedA[j] == prev:
                j += 1
                continue


            elif sortedA[j] != A[i]:
                counter = Counter(A[i + 1:])

                n = lenA - i - 1
                ans += self.getfactorial(n, counter)
            else:
                check = True
                bool[j] = 0
                i += 1
                j = -1
            j += 1

        return (ans + 1) % 1000003


inp = "bbaa"
out = Solution().findRank(inp)
print(out)

'''
baba

aabb
i,j = 0,0

aabb
abab
abba
baab
baba
bbaa


'''
