# /binary Search- https://www.interviewbit.com/problems/rotated-sorted-array-search/


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    # with recursion, TC - O(logn)
    def search1(self, mat, target):
        l, r = 0, len(mat) - 1
        return self.helper(mat, l, r, target)

    def helper(self, mat, l, r, target):
        if l > r:
            return -1
        mid = (l + r) // 2
        if mat[mid] == target:
            return mid
        if mat[l] <= mat[mid]:
            if mat[l] <= target <= mat[mid - 1]:
                return self.helper(mat, l, mid - 1, target)
            return self.helper(mat, mid + 1, r, target)
        if mat[r] >= mat[mid]:
            if mat[mid] <= target <= mat[r]:
                return self.helper(mat, mid + 1, r, target)
            return self.helper(mat, l, mid - 1, target)

    # interative, TC - O(logn)
    def search(self, mat, target):
        l = 0
        r = len(mat) - 1

        while l <= r:
            mid = (l + r) // 2
            if mat[mid] == target:
                return mid
            if mat[l] <= mat[mid]:
                if mat[l] <= target < mat[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if mat[mid] < target <= mat[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

inpA, inpB = [3], 7
out = Solution().search(inpA, inpB)
print(out)
