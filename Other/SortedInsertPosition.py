# Binary Search- https://www.interviewbit.com/problems/sorted-insert-position/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # Proof- Binary search will try to shorted the array search changing l,r, and look for target match, iof not,
    # it will reduce array and check for target position at extremes
    def searchInsert(self, A, B):
        n = len(A)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            # next two if statements to see if target is not away from extremes
            if B < A[l]:
                return l
            if B > A[r]:
                return r + 1
            if A[mid] == B:
                return mid
            if A[mid] < B:
                l = mid + 1
            else:
                r = mid - 1

        return n


inpA, inpB = [2], 3
out = Solution().searchInsert(inpA, inpB)
print(out)
