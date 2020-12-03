'''
https://www.interviewbit.com/problems/sudoku/
Microsoft Qualcomm

Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.

A sudoku puzzle,
(image)
and its solution numbers marked in red.
(image)

Example :
For the above given diagrams, the corresponding input to your program will be

[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
'''

from math import sqrt


class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        if self.validSudoku(A):
            return

        l = [0, 0]
        next_empty_cell = self.findNextEmpty(A, l)

        if not next_empty_cell:
            return

        row, col = l[0], l[1]
        for num in range(1, 10):
            if self.isSafe(A, row, col, num):
                self.assignToCell(A, row, col, num)
                self.solveSudoku(A)
                self.assignToCell(A, row, col, '.')

        return

    # inplace replacement of l with next empty cell row and col.
    def findNextEmpty(self, board, position):
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][0][c] == '.':
                    position[0], position[1] = r, c
                    return True

        return False

    # returns return, if cells in same row, or same col, or inside the box of n*n has same value. Else return true.
    def isSafe(self, board, r, c, val):
        return self.rowSafe(board, r, val) and self.colSafe(board, c, val) and self.safeInBox(board, r, c, val)

    # return False if val present in same row, else return True
    def rowSafe(self, board, r, val):
        for i in range(len(board)):
            if board[r][0][i] == str(val):
                return False

        return True

    # return False if val present in same col, else return True.
    def colSafe(self, board, c, val):
        for i in range(len(board)):
            if board[i][0][c] == str(val):
                return False

        return True

    # return False if val present in n*n box, else return True
    def safeInBox(self, board, r, c, val):
        l = len(board)
        n = int(sqrt(l))
        r, c = r - (r % n), c - (c % n)

        for i in range(n):
            for j in range(n):
                if board[r + i][0][c + j] == str(val):
                    return False

        return True

    # assign value to empty cell.
    def assignToCell(self, board, r, c, value):
        if c == len(board) - 1:
            board[r][0] = board[r][0][:c] + str(value)
        else:
            board[r][0] = board[r][0][:c] + str(value) + board[r][0][c + 1:]

    def validSudoku(self, board):
        n = len(board)

        # check valid row
        for r in range(n):
            dict = {}
            for c in range(n):
                if board[r][0][c] == '.':
                    return False
                elif board[r][0][c] not in dict:
                    dict[board[r][0][c]] = 1
                else:
                    return False

        # check valid col
        for c in range(n):
            dict = {}
            for r in range(n):
                if board[r][0][c] == '.':
                    return False
                elif board[r][0][c] not in dict:
                    dict[board[r][0][c]] = 1
                else:
                    return False

        # check valid box
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                dict = {}
                for i in range(int(sqrt(n))):
                    if board[r + i][0][c + i] == '.':
                        return False
                    elif board[r + i][0][c + i] not in dict:
                        dict[board[r + i][0][c + i]] = 1
                    else:
                        return False

        return True


if __name__ == "__main__":
    # b = [["534678914"], ["672195348"], ["198342567"], ["859761423"], ["426853791"], ["713924856"], ["961537284"], ["287419635"], ["345286179"]]
    # Solution().assignToCell(b,0,0,'.')
    # print(Solution().safeInBox(b,0,0,5))

    board = [
        ["53..7...."],
        ["6..195..."],
        [".98....6."],
        ["8...6...3"],
        ["4..8.3..1"],
        ["7...2...6"],
        [".6....28."],
        ["...419..5"],
        ["....8..79"]
    ]
    Solution().solveSudoku(board)
    print(board)
