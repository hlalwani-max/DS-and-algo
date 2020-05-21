# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.helper(max(nums), nums)

    def helper(self, _max, arr):
        new_node = TreeNode(val = _max)
        _break = arr.index(_max)

        left_arr = arr[:_break]
        right_arr = arr[_break+1:]

        if len(left_arr) > 0:
            new_node.left = self.helper(max(left_arr), left_arr)

        if len(right_arr) > 0:
            new_node.right = self.helper(max(right_arr), right_arr)
        return new_node