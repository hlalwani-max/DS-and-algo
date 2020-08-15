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
