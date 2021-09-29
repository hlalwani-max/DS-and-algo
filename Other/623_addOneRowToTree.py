# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5
'''

class Solution:
    def addOneRow(self, root, v: int, d: int):
        if d == 1:
            temp = root
            root = TreeNode(v)
            root.left = temp
            return root
        self.helper(root, v, d, 1)
        return root

    def helper(self, node, v, d, h):
        if d == h + 1:
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(v)
            node.left.left = old_left
            node.right = TreeNode(v)
            node.right.right = old_right

        else:
            if node.left:
                self.helper(node.left, v, d, h + 1)
            if node.right:
                self.helper(node.right, v, d, h + 1)

        return node