'''
Two Pointer - https://www.interviewbit.com/problems/sort-by-color/

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :
Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
'''

from collections import Counter


class Solution:
    # @param A : list of integers
    # @return A after the sort
    # TC- O(2N), SC- O(1)
    def sortColors(self, A):
        N = len(A)
        count = [0, 0, 0]

        for i in range(N):
            if A[i] == 0:
                count[0] += 1
            elif A[i] == 1:
                count[1] += 1
            elif A[i] == 2:
                count[2] += 1

        ind = 0
        for i in range(3):
            for j in range(count[i]):
                A[ind] = i
                ind += 1

        return A

    # TC - O(3N), SC- O(N)
    def sortColors1(self, A):
        counter = Counter(A)
        ind = 0

        for i in range(len(counter.keys())):
            for j in range(counter[i]):
                A[ind] = i
                ind += 1
        return A

    # TC - O(N^2), SC- O(1)
    def sortColors2(self, A):
        def swap(arr, ind1, ind2):
            tmp = arr[ind1]
            arr[ind1] = arr[ind2]
            arr[ind2] = tmp

        if not A: return 0
        N = len(A)

        for i in range(N):
            for j in range(i, N):
                if A[j] < A[i]:
                    swap(A, i, j)
        return A


if __name__ == "__main__":
    arr = [2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 2, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1,
           0, 2, 2, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 0, 1, 1, 0, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1,
           0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 2, 1, 2,
           2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2]
    out = Solution().sortColors(arr)
    print(out)
