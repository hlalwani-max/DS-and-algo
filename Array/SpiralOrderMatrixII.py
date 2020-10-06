'''
https://www.interviewbit.com/problems/spiral-order-matrix-ii/
Microsoft JPMorgan Amazon
[Medium-Hard] Concept- iteration

Problem-
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input Format:
The first and the only argument contains an integer, A.

Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.

Constraints:
1 <= A <= 1000

Examples:

Input 1:
    A = 3
Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    A = 4
Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
'''

from Array import print2DMatrix


class Direction:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Solution:
    # @param A : integer
    # @return a list of list of integers
    # Idea- start filling numbers in appropriate order- LEFT, DOWN, LEFT, RIGHT (repeat).
    # Modify the 'top, right, bottom, left' markers as you go, avoid leaks. (read code, obvious explanation.)
    # TC- O(N^2), SC- O(N^2)
    def generateMatrix(self, A):
        ans = [[None] * A for _ in range(A)]
        direction = Direction.RIGHT
        start_val = 1
        end_val = A ** 2

        # initialize - top, right, bottom, left
        t, r, b, l = 0, A - 1, A - 1, 0

        # manipulate above markers in particular conditions. Also check if boundaries overflow (sanity check).
        while start_val <= end_val:
            if direction == Direction.RIGHT:
                for i in range(l, r + 1):
                    ans[t][i] = start_val
                    start_val += 1
                t += 1

            elif direction == Direction.DOWN:
                for i in range(t, b + 1):
                    ans[i][r] = start_val
                    start_val += 1
                r -= 1

            elif direction == Direction.LEFT:
                for i in range(r, l - 1, -1):
                    ans[b][i] = start_val
                    start_val += 1
                b -= 1
            else:
                for i in range(b, t - 1, -1):
                    ans[i][l] = start_val
                    start_val += 1
                l += 1

            # repeat directions - LEFT, DOWN, LEFT, RIGHT (repeat)
            direction = (direction + 1) % 4

        return ans


if __name__ == "__main__":
    K = 5
    ans = Solution().generateMatrix(K)

    print("Spiral matrix:")
    print2DMatrix(ans)
