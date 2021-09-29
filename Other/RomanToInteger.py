'''
String- https://www.interviewbit.com/problems/roman-to-integer/

Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20

Idea - Keep adding value of roman, if previous roman is lesser than current, decrement twice of previous (to actually subtract it from answer).
'''


class Solution:
    # @param A : string
    # @return an integer
    # TC- O(n), SC- O(1)
    def romanToInt(self, A):
        ri_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(A)

        if n == 0:
            return 0

        prev, ans = ri_map[A[0]], ri_map[A[0]]

        for i in range(1, n):
            ans += ri_map[A[i]]
            if ri_map[A[i]] > ri_map[A[i - 1]]:
                ans -= (2 * prev)
            prev = ri_map[A[i]]

        return ans


if __name__ == "__main__":
    str = "XIV"
    out = Solution().romanToInt(str)
    print(out)
