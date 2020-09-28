'''
Two Pointers - https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    # TC- O(N), SC- O(1)
    # Idea- i moves to swap with repeating elements, while j moves to find non repeating elements in the list.
    def removeDuplicates(self, A):
        N = len(A)
        i = 0
        j = 1
        while j < N:
            if A[i] == A[j]:
                j += 1
            else:
                if i + 1 < N:
                    tmp = A[i + 1]
                    A[i + 1] = A[j]
                    A[j] = tmp
                    j += 1
                    i += 1
                else:
                    j += 1
        return i + 1


if __name__ == "__main__":
    arr = [1, 1, 2]
    out = Solution().removeDuplicates(arr)
    print(out)