class Solution:
    something = ""

    def binarySearch(self, arr, target, l, r):
        if self.something == "Found":
            return
        if l > r:
            # self.something = "Not found!!"
            return
        mid = (l + r) // 2
        if target == arr[mid]:
            self.something = "Found"
            return
        if target > arr[mid]:
            self.binarySearch(arr, target, mid + 1, r)
        else:
            self.binarySearch(arr, target, l, mid - 1)


sol = Solution()
arr = [1, 2, 3, 4, 5]
target = 4
start = 0
end = len(arr) - 1
sol.binarySearch(arr, target, 0, end)
if sol.something == "Found":
    print("Found")
else:
    print("Not found!!")
