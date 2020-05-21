class Solution:
    def binarySearch(self, arr, target, l, r):
        if l > r:
            return "Not found!!"
        mid = (l + r) // 2
        if target == arr[mid]:
            return "Found!!"
        if target > arr[mid]:
            return self.binarySearch(arr, target, mid + 1, r)
        else:
            return self.binarySearch(arr, target, l, mid - 1)


sol = Solution()
arr = [1, 2, 3, 4, 5]
target = 6
start = 0
end = len(arr) - 1
print(sol.binarySearch(arr, target, 0, end))