'''
String - https://www.interviewbit.com/problems/add-binary-strings/

Given two binary strings, return their sum (also a binary string).

Example:
a = "100"
b = "11"
Return a + b = “111”.

Addition Rules-
0 + 0 = 0
0 + 1 = 1
1 + 1 = 0 (carry 1)
1 + 1 + carry(1) = 1 (carry 1)
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    # TC- O(max(A, B)), SC = O(max(A, B))
    def addBinary(self, A, B):
        m, n = len(A), len(B)
        # print(m, n)
        if m > n:
            for i in range(abs(m - n)):
                B = "0" + B

        elif n > m:
            for i in range(abs(m - n)):
                A = "0" + A

        carry = 0
        ans = ""
        length = len(A)
        i = length - 1

        # print(len(A), len(B))
        # print(A, B)

        while i >= 0:
            sum = int(A[i]) + int(B[i]) + carry

            if sum == 0 or sum == 1:
                ans = str(sum) + ans
                if carry == 1: carry = 0
            elif sum == 2:
                carry = 1
                ans = str(0) + ans
            else:
                carry = 1
                ans = str(1) + ans

            i -= 1

        if carry == 1:
            ans = str(1) + ans
        return ans


if __name__ == "__main__":
    bStr1 = "1010110111001101101000"
    bStr2 = "1000011011000000111100110"
    out = Solution().addBinary(bStr1, bStr2)
    print(out)
