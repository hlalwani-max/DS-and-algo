'''
https://www.interviewbit.com/problems/nqueens/
Qualcomm Google Amazon

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution():
    # @param A : integer
    # @return a list of list of strings
    # TC- O(2^ (N^2)*N), SC- O(2^ (N^2)), since two choices possible if queen is in the spot or not.
    def solveNQueens(self, A):
        self._n = A
        board = [['.' for i in range(A)] for j in range(A)]
        solutions = []
        _n = A
        col = 0
        self.solve(board, col, solutions, _n)
        return solutions

    def solve(self, board, col, solutions, _n):
        if col == _n:
            res = ["".join(row) for row in board]
            solutions.append(res)
            return

        for i in range(_n):

            if self.isSafe(board, i, col, _n):
                board[i][col] = 'Q'

                self.solve(board, col + 1, solutions, _n)

                board[i][col] = '.'
        return

    def isSafe(self, board, row, col, _n):
        if board[row][col] == 'Q':
            return False

        for i in range(_n):
            if board[row][i] == 'Q':
                return False

        # scan upper left diagonal for queen
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # scan lower left diagonal for queen
        for i, j in zip(range(row, _n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # not check upper right and lower right diagonal because we are putting queens in columns going forward,
        # so we only need to check behind.

        '''
        # upper right diagonal check
        for i, j in zip(range(row, -1, -1), range(col, _n)):
            if board[i][j] == 'Q':
                return False

        # lower right diagonal check
        for i, j in zip(range(row, _n), range(col, _n)):
            if board[i][j] == 'Q':
                return False
        '''

        return True


if __name__ == "__main__":
    n = 4
    out = Solution().solveNQueens(n)
    print("Possible solutions for {} queens in {}x{} board is:\n {}".format(n, n, n, out))

