# Math- https://www.interviewbit.com/problems/largest-coprime-divisor/
# Solution Approach- https://www.geeksforgeeks.org/largest-number-divides-x-co-prime-y/'

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

    # @param A : integer
    # @param B : integer
    # @return an integer
    # Time complexity - O(log(logN))
    def cpFact(self, A, B):

        while A > 0:
            gcd = self.gcd(A, B)
            if gcd == 1:
                return A
            A = A // gcd

        return -1

inpA, inpB = 14, 28
out = Solution().cpFact(inpA, inpB)
print(out)
