'''
String- Reverse the string- https://www.interviewbit.com/problems/reverse-the-string/

Given a string A.
Return the string A after reversing the string word by word.

NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"

Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
'''


class Solution:
    # @param A : string
    # @return a strings
    # TC - O(N), SC- O(N)
    def solve(self, A):
        ans = ""
        words = A.split(" ")

        for i in range(len(words) - 1, -1, -1):
            str = words[i].strip()
            if str != "":
                ans += (words[i].strip() + " ")

        if len(ans) == 0: return ""
        return ans[:-1]


if __name__ == "__main__":
    str = "the sky is blue"
    out = Solution().solve(str)
    print("Reversal of input words of '{}' is: {}".format(str, out))
