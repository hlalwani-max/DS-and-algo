# Math- https://www.interviewbit.com/problems/square-root-of-integer/
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A

        l = 1
        r = A

        while l <= r:
            mid = (l + r) // 2

            if mid * mid == A:
                return mid
            # to get floor value
            elif mid * mid < A:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        return ans


inp = 17
out = Solution().sqrt(inp)
print(out)
