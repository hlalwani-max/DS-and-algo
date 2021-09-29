# Math- https://www.interviewbit.com/problems/city-tour/

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        b = len(B)
        visited = [0] * (A+1)
        for i in range(b):
            visited[B[i]] = 1

 