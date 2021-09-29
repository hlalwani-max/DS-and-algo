# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array98.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
# Note:
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.
# This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes = []

        def dfs(root):
            if root:
                nodes.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        nodes.sort()
        # print(nodes)
        diff = [nodes[i + 1] - nodes[i] for i in range(len(nodes) - 1)]
        # print(diff)
        return min(diff)

'''
# Solution2 using inorder nature of BST
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                
                self.minimum = min(self.minimum, root.val - self.prev)
                self.prev = root.val
                
                inorder(root.right)
        
        self.minimum = float("inf")
        self.prev = float("-inf")
        inorder(root)
        
        return self.minimum
'''