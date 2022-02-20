class Solution:
    def binarySearch(self, arr, target, l, r):
        if l > r:
            return False
        mid = (l + r) // 2
        if target == arr[mid]:
            return True
        if target > arr[mid]:
            return self.binarySearch(arr, target, mid + 1, r)
        else:
            return self.binarySearch(arr, target, l, mid - 1)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        columnCount = len(matrix[0])
        for i in range(len(matrix)):
            # print(matrix[i])
            flag = self.binarySearch(matrix[i], target, 0, columnCount - 1)
            if flag:
                return True

        return False

sol = Solution()
inp = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 31
print(sol.searchMatrix(inp,target))