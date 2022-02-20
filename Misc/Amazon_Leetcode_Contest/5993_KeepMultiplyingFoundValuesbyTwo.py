class Solution:
    def findFinalValue(self, nums, original):
        dict = {}

        for item in nums:
            if item not in dict:
                dict[item] = 1

        while original in dict and dict[original] == 1:
            dict[original] = 0
            original *= 2

        return original


nums, original = [2, 7, 9], 4
ans = Solution().findFinalValue(nums, original)
print(ans)
