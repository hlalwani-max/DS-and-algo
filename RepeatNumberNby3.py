# Array- https://www.interviewbit.com/problems/n3-repeat-number/

import collections


class Solution:

    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A.sort()
        lA = len(A)
        N = int(lA / 3)

        i = 0
        curr = None
        while i < lA:
            if not curr:
                curr = A[i]
                count = 1
                i += 1
            else:
                while i < lA:
                    if A[i] != curr:
                        curr = None
                        i += 1
                        break
                    else:
                        count += 1

                    if count > N:
                        return A[i]
                    i += 1
        return -1

    # with space complexity- O(N)
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber1(self, A):
        lA = len(A)
        counter = collections.Counter(A)
        N = int(lA / 3)

        for key in counter.keys():
            if counter[key] > N:
                return key

        return -1


inp = [0, 0, 0, 1, 2, 3, 4]
out = Solution().repeatedNumber(inp)
print(out)
