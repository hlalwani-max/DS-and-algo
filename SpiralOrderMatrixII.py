class Solution:
    # @param A : integer
    # @return a list of list of integers

    def spiralMatrix(self, ):
        pass

    def generateMatrix(self, A):
        x, y = 0
        order = ["right", "down", "left", "up"]

        map= {
            "right": x+1,
            "down": y-1,
            "left": x-1,
            "up": y+1
        }

        ans = [[None] * A] * A



        return ans


if __name__ == "__main__":
    sol = Solution()
    inp = 3
    print("Input: ", inp)
    ans = sol.generateMatrix(inp)
    print("Output: ", ans)
