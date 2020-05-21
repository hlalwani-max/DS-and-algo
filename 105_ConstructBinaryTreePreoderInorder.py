# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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



'''
#working code Karan short
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:ind + 1], inorder[:ind])
        root.right = self.buildTree(preorder[ind + 1:], inorder[ind + 1:])

        return root

'''


class Solution:
    pre_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return
        if self.pre_index >= len(preorder):
            return
        root = TreeNode(preorder[self.pre_index])

        #     # split inorder
        ind = inorder.index(preorder[self.pre_index])
        sub_left = inorder[:ind]
        sub_right = inorder[ind + 1:]
        l_sub_left = len(sub_left)
        l_sub_right = len(sub_right)

        if l_sub_left == 1:
            self.pre_index += 1
            root.left = TreeNode(sub_left[0])

        if l_sub_left > 1:
            self.pre_index += 1
            root.left = self.buildTree(preorder, sub_left)

        if l_sub_right == 1:
            self.pre_index += 1
            root.right = TreeNode(sub_right[0])

        if l_sub_right > 1:
            self.pre_index += 1
            root.right = self.buildTree(preorder, sub_right)

        return root
