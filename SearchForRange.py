# Binary Search- https://www.interviewbit.com/problems/search-for-a-range/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    # Time complexity- O(2*logN), because we are running binary search hop on two sides of the array
    def searchRange(self, A, B):

        def binarysearch(A, l, r, B, arr, flag):
            while l <= r:
                mid = (l + r) // 2
                if A[mid] == B:
                    if flag:  # continue for left array if flag True
                        arr[0] = mid
                        r = mid - 1
                    else:  # continue for right array if flag False
                        arr[1] = mid
                        l = mid + 1
                elif A[mid] > B:
                    r = mid - 1
                else:
                    l = mid + 1

        ans = [-1, -1]
        n = len(A)
        l, r = 0, n - 1

        binarysearch(A, l, r, B, ans, True)  # to find begin (go left)
        binarysearch(A, l, r, B, ans, False)  # to find end (go rught)
        return ans

    # Time Complexity- O(N), if all elements are same
    def searchRange1(self, A, B):
        n = len(A)

        l, r = 0, n - 1
        ans = [-1, -1]

        while l <= r:
            mid = (l + r) // 2
            if A[mid] == B:
                ans = [mid, mid]

                # find similar elements to left
                start = mid - 1
                while start >= 0 and A[start] == B:
                    ans[0] = start
                    start -= 1

                # find similar elements to right
                end = mid + 1
                while end < n and A[end] == B:
                    ans[1] = end
                    end += 1
                return ans

            if A[mid] < B:
                l = mid + 1
            else:
                r = mid - 1
        return ans


inp = [5, 7, 7, 8, 8, 10]
B = 7
out = Solution().searchRange(inp, B)
print(out)
