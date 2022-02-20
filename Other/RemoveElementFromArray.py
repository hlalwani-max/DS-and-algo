'''
Two Pointer - https://www.interviewbit.com/problems/remove-element-from-array/

Remove Element

Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # TC- O(N), SC- O(1)
    def removeElement(self, A, B):
        j = 0
        # Find elements not B and put them in the begining of the array.
        # i pointer traverse array and look for 'not B', while j pointer find the next position to put the value into.
        for i in range(len(A)):
            if A[i] != B:
                A[j] = A[i]
                j += 1
        # value of j is where we traversed the list and removed B, plus 1.
        # delete remaining to change A
        del (A[j:])
        return j

    # TC- O(N), SC- O(N)
    def removeElement1(self, A, B):
        res = []
        for i in range(len(A)):
            if A[i] != B:
                res.append(A[i])

        ans = len(res)
        for i in range(ans):
            A[i] = res[i]

        return ans


if __name__ == "__main__":
    arr, target = [1, 2, 3, 2], 2
    out = Solution().removeElement(arr, target)
    print(out)
