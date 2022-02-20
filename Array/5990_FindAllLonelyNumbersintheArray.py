class Solution:
    '''
        O()
    '''

    def findLonely(self, nums):
        dict = {}
        lonelyNums = []

        # save elements in dictionary w/ frequencies for easy lookup
        for item in nums:
            if item not in dict:
                dict[item] = 1
            else:
                dict[item] += 1

        # find lonely numbers in the original list and look in dictionary for condition checks
        for item in nums:
            if dict[item] == 1 and item - 1 not in dict and item + 1 not in dict:
                lonelyNums.append(item)

        return lonelyNums


input = [10, 6, 5, 8]
output = Solution().findLonely(input)
print(output)
