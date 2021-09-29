# Binary Search - https://www.interviewbit.com/problems/matrix-search/

class Solution:
    def binarysearch(self, arr, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return 1
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return 0


    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        N, M = len(A), len(A[0])

        # if element out of range(min,max), return 0
        if not A[0][0] <= B <= A[N-1][M-1]:
            return 0

        # if elements are at extremes, return 1
        if A[0][0] == B or A[N-1][M-1] == B:
            return 1

        for i in range(N):
            if A[i][0] <= B <= A[i][M-1]:
                return self.binarysearch(A[i], 0, M-1, B)
        return 0


A = [[1, 3, 5, 7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]
B = 33
out = Solution().searchMatrix(A, B)
print(out)
