# Array- https://www.interviewbit.com/problems/noble-integer/

'''
Given an integer array A, find if an integer p exists in the array such that the number of integers
greater than p in the array equals to p.

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is found else return -1.

Example Input
Input 1:
 A = [3, 2, 1, 3]
Input 2:
 A = [1, 1, 3, 3]

Example Output
Output 1:
 1
Output 2:
 -1
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)

        def getcount(l, ind):
            return l - ind - 1

        for i in range(n):
            if i + 1 < n - 1 and A[i] == A[i + 1]:
                continue

            count = getcount(n, i)
            p = A[i]
            if count == p:
                return 1

        return -1


if __name__ == "__main__":
    inp = [3, 2, 1, 3]
    out = Solution().solve(inp)
    print(out)
