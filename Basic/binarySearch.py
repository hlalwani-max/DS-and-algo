'''
Problem-
use binary search to find target in an sorted array in logN time.
'''


class Solution:
    _something = ""

    # using recursion
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

if __name__ == "__main__":
    sol = Solution()
    # sorted array as input.
    arr = [1, 2, 3, 4, 5]
    target = 7
    start, end = 0, len(arr) - 1
    out = sol.binarySearch(arr, target, 0, end)
    print(out)
