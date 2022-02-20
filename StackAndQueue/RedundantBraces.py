'''
https://www.interviewbit.com/problems/redundant-braces/
Amazon

Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
Check whether A has redundant braces or not.
Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.


Input Format
The only argument given is string A.

Output Format
Return 1 if string has redundant braces, else return 0.

For Example
Input 1:
    A = "((a + b))"
Output 1:
    1
Explanation 1:
    ((a + b)) has redundant braces so answer will be 1.

Input 2:
    A = "(a + (a + b))"
Output 2:
    0
Explanation 2:
    (a + (a + b)) doesn't have have any redundant braces so answer will be 0.
'''


class Solution:
    # @param A : string
    # @return an integer
    # TC- O(2N), SC- O(N)
    # Idea- add to stack until ")" found. When ")" found, keep popping from stack until "(" and maintain count of characters in between.
    # If count < 2, redundant space found. Else, when string finished, no redundant spaces.
    def braces(self, A):
        stack = []
        for i in range(len(A)):
            # skip if spaces found.
            if A[i] == " ":
                continue
            if A[i] == ")":
                c = 0
                while stack:
                    ele = stack.pop()
                    if ele == "(":
                        break
                    elif ele == " ":
                        continue
                    else:
                        c += 1
                if c < 2:
                    return 1
            else:
                stack.append(A[i])

        return 0


if __name__ == "__main__":
    str = "(a + (a + b))"
    out = Solution().braces(str)
    print("Redundant braces found." if out == 1 else "No redundant braces found.")
