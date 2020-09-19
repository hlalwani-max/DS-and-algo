'''
String-  https://www.interviewbit.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Given s = "Hello World",
return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
'''


class Solution:
    # @param A : string
    # @return an integer
    # TC = O(N)
    # Hint- Reverse traverse array(handle spaces in the end), and look if word found return length, else find word
    def lengthOfLastWord(self, A):

        ans = 0
        for i in range(len(A) - 1, -1, -1):
            if A[i] == " ":
                if ans > 0:
                    return ans
                else:
                    continue
            else:
                ans += 1

        # for cases - "d"
        if ans > 0:
            return ans
        else:
            return 0


if __name__ == "__main__":
    inp = "Hello World"
    out = Solution().lengthOfLastWord(inp)
    print(out)