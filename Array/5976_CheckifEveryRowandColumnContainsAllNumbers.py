class Solution:
    def isValidList(self, arr, l):
        dict = {}
        for i in range(1, l + 1):
            dict[i] = 1

        for i in arr:
            if dict[i] == 0:
                return False
            else:
                dict[i] = 0

        return True

    def checkValid(self, matrix):
        l = len(matrix[0])

        for i in range(l):
            # check row
            if self.isValidList(matrix[i], l) is False:
                return False

        for i in range(l):
            col = []
            for j in range(l):
                col.append(matrix[j][i])

            # check column
            if self.isValidList(col, l) is False:
                return False

        return True


# inp = [[1,1,1],[1,2,3],[1,2,3]]
inp = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
ans = Solution().checkValid(inp)
print(ans)
