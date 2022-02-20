class Solution:
    def minSwaps(self, nums):
        # find the biggest group of 1s
        l = len(nums)
        prev_len = 0
        start, end, len = 0, 0, 0
        desiredGroup = []
        while (start < l):
            if nums[start] == 1:
                end = start
                while end + 1 < l and nums[end + 1] == 1:
                    end += 1
                    len += 1
                # if group found, save it:
                if len > prev_len:
                    desiredGroup.append([start, end])


inp = [0, 1, 0, 1, 1, 0, 0]
ans = Solution().minSwaps(inp)
print("Min swaps: ", ans)
