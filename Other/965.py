# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        return self.helper(root, value, True)
        # return

    def helper(self, root, value, _bool):
        if root:
            if root.val != value:
                _bool = False
                return _bool
            _bool = self.helper(root.left, value, _bool) and self.helper(root.right, value, _bool)

        return _bool
