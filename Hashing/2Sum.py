'''
https://www.interviewbit.com/problems/2-sum/
Facebook Amazon Google
Concept- One pass hashtable.

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    # TC- O(N), SC- O(1)
    # Idea - One pass hash table. All constraints for the problem with match including duplicate values,
    # minimum index2, minimum index 1 if index2 are same.
    # Refer: https://leetcode.com/problems/two-sum/solution/
    def twoSum(self, A, B):
        N = len(A)
        dict = {}
        ans = []

        for i in range(N):
            tar = B - A[i]

            # find if a B - A[i] exists before.
            if tar in dict.keys():
                ind1, ind2 = dict[tar], i + 1
                return [ind1, ind2]
            # if duplicate value found, it will save one with minimum index
            if A[i] not in dict:
                dict[A[i]] = i + 1
        return ans


if __name__ == "__main__":
    arr, target = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4,
                   -8], -3
    out = Solution().twoSum(arr, target)
    print("The following index to the target sum is: {}".format(out))
