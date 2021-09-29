# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        self.post_index = len(postorder) - 1
        if self.post_index == -1:
            return

        return self.helper(inorder, postorder)

    def helper(self, inorder, postorder):
        if self.post_index < 0:
            return
        root = TreeNode(postorder[self.post_index])

        #     # split inorder
        ind = inorder.index(postorder[self.post_index])
        sub_left = inorder[:ind]
        sub_right = inorder[ind + 1:]
        l_sub_left = len(sub_left)
        l_sub_right = len(sub_right)

        if l_sub_right == 1:
            self.post_index -= 1
            root.right = TreeNode(sub_right[0])

        if l_sub_right > 1:
            self.post_index -= 1
            root.right = self.helper(sub_right, postorder)

        if l_sub_left == 1:
            self.post_index -= 1
            root.left = TreeNode(sub_left[0])

        if l_sub_left > 1:
            self.post_index -= 1
            root.left = self.helper(sub_left, postorder)

        return root
