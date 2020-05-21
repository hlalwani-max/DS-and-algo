# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self, a, b):
        la = len(a)
        if la != len(b):
            return False
        for i in range(la):
            if a[i] != b[i]:
                return False
        return True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False

        val1 = []
        val2 = []
        self.helper(p, val1)
        self.helper(q, val2)
        return self.check(val1, val2)

    def helper(self, a, value):
        if a:
            value.append(a.val)
            self.helper(a.left, value)
            self.helper(a.right, value)


