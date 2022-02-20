class Solution:
    def countElements(self, nums):
        output = 0

        nums = sorted(nums)
        for i in range(1, len(nums) - 1):
            if (nums[i] > nums[0] and nums[i] < nums[-1]):
                output += 1

        return output


input = [11, 7, 2, 15]
output = Solution().countElements(input)
print(output)
