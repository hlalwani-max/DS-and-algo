'''
Two Pointer - https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.
Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],
Your function should return length = 3, and A is now [1,1,2].
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        N = len(A)
        if N <= 2: return A

        i, j = 0, 1
        count = 1

    # My solution [Works] - TC= O(N)
    def removeDuplicates1(self, A):
        N = len(A)

        def swap(arr, ii, jj):
            tmp = arr[ii]
            arr[ii] = arr[jj]
            arr[jj] = tmp

        dcheck = True
        i, j = 0, 0
        while i < N and j < N:
            if i + 1 < N and dcheck and A[i] == A[i + 1]:
                i += 1
                dcheck = False
                continue
            if A[j] != A[i]:
                dcheck = True
                val = A[j]
                if i + 1 < N:
                    swap(A, i + 1, j)
                if i + 2 < N and j + 1 < N and A[j + 1] == val:
                    swap(A, i + 2, j + 1)
                    j += 1
                i += 1
                j += 1
            else:
                j += 1

        if i + 1 < N and dcheck and A[i] == A[i + 1]: i += 1
        A = A[:i + 1]
        # print(A)
        return i + 1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 2, 3, 3, 3, 3]
    out = Solution().removeDuplicates(arr)
    print(out)
