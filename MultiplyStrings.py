'''
[Microsoft, Google]
String: Multiply two strings as normal number multiplication- https://www.interviewbit.com/problems/multiply-strings/

Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings

    def multiply(self, A, B):
        m, n = len(A), len(B)
        pass
    
    # My solution- Condition A is in integer range, TC - O(N)
    def multiply1(self, A, B):
        m, n = len(A), len(B)
        count = 0
        tmp = []
        for i in range(n - 1, -1, -1):
            cur = (int(A) * int(B[i]))
            if count > 0: cur *= (10 ** count)
            count += 1
            tmp.append(cur)
        return sum(tmp)


if __name__ == "__main__":
    str1, str2 = "12", "100"
    out = Solution().multiply(str1, str2)
    print(out)
