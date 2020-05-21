# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        leftRes = []
        rightRes = []
        children = []

        def leftBoundary(root):
            if root:
                leftRes.append(root.val)

                if not root.left:
                    leftBoundary(root.right)
                else:
                    leftBoundary(root.left)

        def findLeaves(root):
            if root:
                if not root.left and not root.right:
                    children.append(root.val)
                findLeaves(root.left)
                findLeaves(root.right)

        def rightBoundary(root):
            if root:
                if not root.right:
                    rightBoundary(root.left)
                else:
                    rightBoundary(root.right)
                rightRes.append(root.val)

        if not root:
            return []

        if root.left:
            leftBoundary(root.left)

        if root.left or root.right:
            findLeaves(root)

        if root.right:
            rightBoundary(root.right)

        return [root.val] + leftRes[:-1] + children + rightRes[1:]
