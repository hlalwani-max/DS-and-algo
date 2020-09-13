# Math- https://www.interviewbit.com/problems/binary-representation/
# return a decimal number in binary

class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A == 0:
            return "0"
        rem = []

        while A > 0:
            rem.append(str(A % 2))
            A = int(A / 2)

        return "".join(rem[::-1])


inp = 6
out = Solution().findDigitsInBinary(inp)
print(out)
