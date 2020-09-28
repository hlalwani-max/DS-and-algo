'''
Two Pointer - https://www.interviewbit.com/problems/intersection-of-sorted-arrays/

Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :
Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]
Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]
Output : [3 5]
'''


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        m, n = len(A), len(B)
        i, j = 0, 0
        ans = []

        while i < m and j < n:
            if A[i] < B[j]:
                i += 1
            elif A[i] > B[j]:
                j += 1
            else:
                ans.append(A[i])
                i += 1
                j += 1

        return ans


if __name__ == "__main__":
    arr1, arr2 = [1, 2, 3, 3, 4, 5, 6], [3, 3, 5]
    out = Solution().intersect(arr1, arr2)
    print(out)
