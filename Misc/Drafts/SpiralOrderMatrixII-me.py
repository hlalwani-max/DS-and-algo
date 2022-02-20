'''
https://www.interviewbit.com/problems/spiral-order-matrix-ii/
Microsoft JPMorgan Amazon
Concept-
Status - Incomplete, code not working as desired.

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


class Solution:
    # @param A : integer
    # @return a list of list of integers

    def giveNextDirection(self, curr, order):
        ind = order.index(curr)
        if ind > 2:
            ind = 0
            return order[ind]
        else:
            return order[ind + 1]

    def check(self, x, y, A, ans):
        if (x < A and y < A) and ans[x][y] is None:
            return True
        else:
            return False

    '''
    def generateMatrix(self, A):
        x, y = 0, 0
        order = ["right", "down", "left", "up"]
        direction = order[0]

        ans = [[None for i in range(A)] for j in range(A)]
        val = 1
        ans[x][y] = val
        val += 1

        self.helper(ans, direction, val, order, A, x, y)

        return ans
    '''

# recursion doesn't work because for larger value of A,  recursion stack limit goes up significantly causing maximum depth of recursion reached error
    '''
    def helper(self, ans, direction, val, order, A, x, y):

        map = {
            "right": (x, y + 1),
            "down": (x + 1, y),
            "left": (x, y - 1),
            "up": (x - 1, y)
        }

        if val > (A ** 2):
            return

        (a, b) = map[direction]

        if self.check(a, b, A, ans):
            x, y = a, b
            ans[x][y] = val
            val += 1
        else:
            direction = self.giveNextDirection(direction, order)
        self.helper(ans, direction, val, order, A, x, y)
    '''


    def generateMatrix(self, A):
        x, y = 0, 0
        order = ["right", "down", "left", "up"]
        direction = order[0]

        map = {
            "right": (x, y + 1),
            "down": (x + 1, y),
            "left": (x, y - 1),
            "up": (x - 1, y)
        }

        ans = [[None for i in range(A)] for j in range(A)]
        val = 1
        ans[x][y] = val
        val += 1

        while val <= A ** 2:
            (a, b) = map[direction]

            if self.check(a, b, A, ans):
                x, y = a, b
                ans[x][y] = val
            else:
                direction = self.giveNextDirection(direction, order)
                (a, b) = map[direction]

                if self.check(a, b, A, ans):
                    x, y = a, b
                    ans[x][y] = val

            val += 1
            print(ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    inp = 4
    print("Input: ", inp)
    ans = sol.generateMatrix(inp)

    print("Output: ")
    for row in ans:
        print(row)
