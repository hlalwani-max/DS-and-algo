'''
Two pointer- https://www.interviewbit.com/problems/3-sum/

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''

import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # TC- O(NlogN)
    # Idea - loop throgh i, use sorting advantage on j and k.
    def threeSumClosest(self, A, B):
        N = len(A)
        A.sort()
        diff = sys.maxsize
        sum = 0
        for i in range(N):
            j, k = i+1, N-1
            while j < k:
                cur_sum = A[i] + A[j] + A[k]
                cur_diff = abs(B - cur_sum)
                if cur_diff == 0:
                    return cur_sum
                if cur_diff < diff:
                    diff = cur_diff
                    sum = cur_sum
                if cur_sum < B:
                    j += 1
                else:
                    k -= 1

        return sum

    #     TC - O(N^3)
    def threeSumClosest1(self, A, B):
        N = len(A)
        A.sort()
        diff = sys.maxsize
        sum = 0
        for i in range(N):
            for j in range(i + 1, N - 2):
                for k in range(j + 1, N):
                    curr_sum = A[i] + A[j] + A[k]
                    curr_diff = curr_sum - B
                    if abs(curr_diff) < diff:
                        sum = curr_sum
                        diff = abs(curr_diff)

        return sum


if __name__ == "__main__":
    arr, target = [-1, 2, 1, -4], 1
    out = Solution().threeSumClosest(arr, target)
    print("Sum of three closest pair is- {}".format(out))
