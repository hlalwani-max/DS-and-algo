class Solution:
    def maxScoreIndices(self, nums):
        length = len(nums)
        max = 0
        dict = {0: [0]}

        for i in range(length + 1):
            if i == 0:
                lNums = []
                rNums = nums
            elif i == length:
                lNums = nums
                rNums = []
            else:
                lNums = nums[:i]
                rNums = nums[i:]

            freqZero = self.getCount(lNums, 0)
            freqOne = self.getCount(rNums, 1)
            count = freqZero + freqOne

            if count >= max:
                if max in dict and count > max:
                    del dict[max]

                if count not in dict:
                    dict[count] = [i]
                else:
                    dict[count].append(i)

                max = count

        return dict[max]

    def getCount(self, arr, target):
        count = 0
        for item in arr:
            if item == target:
                count += 1

        return count


nums = [0, 0, 0]
ans = Solution().maxScoreIndices(nums)
print(ans)
