'''
https://www.interviewbit.com/problems/simplify-directory-path/
Microsoft

Given a string A representing an absolute path for a file (Unix-style).
Return the string A after simplifying the absolute path.

Note:
Absolute path always begin with ’/’ ( root directory ).
Path will not have whitespace characters.

Input Format
The only argument given is string A.

Output Format
Return a string denoting the simplified absolue path for a file (Unix-style).
For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"
'''


class Solution:
    # @param A : string
    # @return a strings
    # TC- O(N), SC- O(N)
    def simplifyPath(self, A):
        path = A.split('/')

        stack = []

        # pop if stack not empty and "..", if ".", do nothing, else add to stack
        for item in path:
            if item in ['', '.']:
                continue
            elif item == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(item)

        # append path in stack.
        res = ''
        for item in stack:
            res += ('/' + item)

        #
        if len(res) == 0:
            return '/'

        return res


if __name__ == "__main__":
    str = "/home//foo/"
    out = Solution().simplifyPath(str)
    print("simplified path: ", out)
