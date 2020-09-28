'''
String: Convert Integer to Roman - https://www.interviewbit.com/problems/integer-to-roman/

Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version.

Constraints
1 <= A <= 3999

For Example
Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"

Idea- Make a decreasing mapping of special combinations, traverse them in decreasing order and update input to reach to
end of the combination list.
'''


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        mapping = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        ans = ""
        for i, val in mapping:
            while A >= i:
                ans += val
                A -= i

        return ans


if __name__ == "__main__":
    val = 423
    out = Solution().intToRoman(val)
    print(out)
