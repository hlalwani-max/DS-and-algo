class Direction:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        ans = [[None] * A for _ in range(A)]
        direction = Direction.RIGHT
        start_val = 1
        end_val = A ** 2
        t, r, b, l = 0, A - 1, A - 1, 0

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

            direction = (direction + 1) % 4

        return ans


if __name__ == "__main__":
    sol = Solution()
    inp = 5
    print("Input: ", inp)
    ans = sol.generateMatrix(inp)

    print("Output: ")
    for row in ans:
        print(row)
