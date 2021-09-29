# Array- https://www.interviewbit.com/problems/set-matrix-zeros/
# Time complexity- O(M*N), O(M+N)

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        row, col = set(), set()
        lA_row, lA_col = len(A), len(A[0])
        for i in range(lA_row):
            for j in range(lA_col):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in row:
            for j in range(lA_col):
                A[i][j] = 0

        for j in col:
            for i in range(lA_row):
                A[i][j] = 0

        return A


arr = [
    [0, 0],
    [1, 0]
]

out = Solution().setZeroes(arr)

for row in out:
    print(row)
