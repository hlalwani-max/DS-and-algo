'''
https://leetcode.com/problems/next-permutation/
Google Bloomberg ByteDance Microsoft Amazon Adobe Uber Apple Flipkart Salesforce

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''


class Solution:
    # TC- O(N), SC- O(1)
    # Idea- find i-1 such that a[i-1] < a[i], swap it with next bigger number on right, reverse element on right of i-1.
    # Refer leetcode solution.
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        N = len(nums)

        # find first non-decreasing element from right. Since, for any given sequence that is in descending order,
        # no next larger permutation is possible.
        target = -1
        for i in range(N - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                target = i - 1
                break

        # if given permutation in decreasing order (target not found), no next permutation possible. Return sorted perm.
        if target == -1:
            self.reverseArray(nums, 0, N - 1)
        else:
            # swap target with next bigger number on right and reverse right element.
            to_swap = target + 1
            for i in range(target, N):
                if nums[i] > nums[target]:
                    to_swap = i

            # print(target, to_swap)
            nums[target], nums[to_swap] = nums[to_swap], nums[target]
            self.reverseArray(nums, target + 1, N - 1)

    def reverseArray(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    # perm = [1, 3, 2]
    perm = [2,3,1,3,3]
    org_perm = list(perm)
    Solution().nextPermutation(perm)
    print("Next permutations for {} is: {}".format(org_perm, perm))
