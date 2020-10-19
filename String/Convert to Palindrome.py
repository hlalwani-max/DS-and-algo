'''
https://www.interviewbit.com/problems/convert-to-palindrome/
Amazon

Concept- Two Pointer

Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

If it is possible then return 1 else return 0.



Problem Constraints
3 <= |A| <= 105

A[i] is always a lowercase character.



Input Format
First and only argument is an string A.



Output Format
Return 1 if it is possible to convert A to palindrome by removing exactly one character else return 0.



Example Input
Input 1:

 A = "abcba"
Input 2:

 A = "abecbea"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 We can remove character ‘c’ to make string palindrome
Explanation 2:

 It is not possible to make this string palindrome just by removing one character
'''


class Solution:
    # @param A : string
    # @return an integer
    # TC- O(N), SC- O(1), only one iteration is done on input string.
    # Idea- start from two sides, if any side A[i] != A[j] is found, remove i or j and test if rest is palindrome.
    def solve(self, A):
        if A[::-1] == A:
            return 1

        i, j = 0, len(A) - 1

        while i < j:
            if A[i] == A[j]:
                i += 1
                j -= 1
                continue
            else:
                # if on any side elements are not equal, we remove both element and test,
                # ie. if removing i or j element, if it's a palindrome, then answer = 1
                s1 = A[i + 1: j + 1]  # i+1 to j
                s2 = A[i:j]  # i to j-1

                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return 1
                else:
                    return 0

            i += 1
            j -= 1

        return 0


if __name__ == "__main__":
    inp_str = "abcba"
    out = Solution().solve(inp_str)
    print("Palindrome possible removing at most 1 character.") if out == 1 else print(
        "Palindrome not possible removing at most 1 character.")
