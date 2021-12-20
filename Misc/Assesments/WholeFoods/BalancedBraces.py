'''
https://www.interviewbit.com/problems/balanced-parantheses/
Amazon Google

Problem-
Given a string A consisting only of '(' and ')'.
You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
First argument is an string A.

Output Format
Return 1 if parantheses in string are balanced else return 0.

Example Input

Input 1:
 A = "(()())"

Input 2:
 A = "(()"

Example Output

Output 1:
 1

Output 2:
 0

Example Explanation
Explanation 1:
 Given string is balanced so we return 1

Explanation 2:
 Given string is not balanced so we return 0
'''


class Solution:
    _braces_mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    _open_braces = ["(", "[", "{"]
    _closed_braces = [")", "]", "}"]

    # @param A : string
    # @return an integer
    # TC- O(N)
    def solve(self, A):
        stack = []
        for character in A:
            if character in self._closed_braces:
                if not stack:
                    return 0

                while stack:
                    if stack.pop() == self._braces_mapping[character]:
                        break
            else:
                stack.append(character)

        if not stack:
            return 1
        else:
            return 0


if __name__ == "__main__":
    input_str = "(()())"
    out = Solution().solve(input_str)
    print("braces balanced!" if out == 1 else "Not braces balanced!!")
