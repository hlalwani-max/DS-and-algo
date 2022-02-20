# Math- https://www.interviewbit.com/problems/trailing-zeros-in-factorial/

# Count number of 5's
class Solution:
    # @param A : integer
    # @return an integer
    # time- O(logN)
    def trailingZeroes(self, A):
        count5 = 0

        while A > 0:
            count5 += A // 5
            A = A // 5

        return count5

    # time complexity- O(NlogN), for 1->N numbers in A
    def trailingZeroes1(self, A):
        count5 = 0
        for i in range(A, 0, -1):
            if i % 5 == 0:
                num = i
                while num > 0 and num % 5 == 0:
                    count5 += 1
                    num = num // 5
                i -= 5

        return count5


inp = 8607
out = Solution().trailingZeroes(inp)
print(out)
