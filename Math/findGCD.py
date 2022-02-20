# Math- https://www.interviewbit.com/problems/greatest-common-divisor/
import sys


class Solution:
    # using euclidian theoram
    def gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a

        tmp = min(a, b)
        a = max(a, b)
        b = tmp

        return self.helper(a, b, sys.maxsize)

    def helper(self, a, b, prev_rem):
        rem = a % b

        if a % b == 0:
            if prev_rem == sys.maxsize:
                return b
            else:
                return prev_rem
        else:
            return self.helper(b, rem, rem)


a, b = 5, 7
out = Solution().gcd(a, b)
print(out)
