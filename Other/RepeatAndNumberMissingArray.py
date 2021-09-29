# Array- https://www.interviewbit.com/problems/repeat-and-missing-number-array/
'''
Solution-
    Sum(Actual) = Sum(1...N) + A - B

    Sum(Actual) - Sum(1...N) = A - B.

    Sum(Actual Squares) = Sum(1^2 ... N^2) + A^2 - B^2

    Sum(Actual Squares) - Sum(1^2 ... N^2) = (A - B)(A + B)

    = (Sum(Actual) - Sum(1...N)) ( A + B).
'''
import collections


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        lA = len(A)
        AMinusB = sum(A) - sum([i for i in range(1, lA + 1)])
        AsqMinusBsq = sum([item ** 2 for item in A]) - sum([i ** 2 for i in range(1, lA + 1)])

        APlusB = AsqMinusBsq / AMinusB

        a = (AMinusB + APlusB) / 2
        b = (AMinusB - APlusB) / 2

        return int(a), -int(b)

    # with space O(N)
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber1(self, A):
        lA = len(A)

        counter = collections.Counter(A)
        for i in range(1, lA + 1):
            if i not in counter.keys():
                B = i
            else:
                if counter[i] == 2:
                    A = i

        return A, B


inp = [3, 1, 3, 2, 5]
A, B = Solution().repeatedNumber(inp)
print(A, B)
