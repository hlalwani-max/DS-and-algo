# Binary search- https://www.interviewbit.com/problems/allocate-books/


# incomplete- wrong answer for A : [ 73, 58, 30, 72, 44, 78, 23, 9 ]
# B : 5, expected 110
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        ans = -1
        n, k = len(A), B

        if k >= n:
            if k == n:
                return max(A)
            else:
                return ans

        A.sort()

        # print(A)
        def getmin(A, v, n):
            sum, count = 0, 1
            i = 0
            while i < n:
                if sum + A[i] > v:
                    sum = A[i]
                    count += 1
                else:
                    sum += A[i]

                i += 1
            return count

        l, r = A[-1], sum(A)

        while l <= r:
            mid = (l + r) // 2
            count = getmin(A, mid, n)
            if B == count:
                ans = mid
                r = mid - 1
            elif B < count:
                l = mid + 1
            else:
                r = mid - 1
        return ans


A, B = [73, 58, 30, 72, 44, 78, 23, 9], 5
out = Solution().books(A, B)
print(out)
