# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
        self.prev = root.val
        return self.helper(root.left, "left") and self.helper(root.right, "right")

    def helper(self, root, str):
        if root:
            left = self.helper(root.left, "left")

            if str == "left":
                if root.val > self.prev:
                    return False

            if str == "right":
                if root.val < self.prev:
                    return False

            self.prev = root.val

            right = self.helper(root.right, "right")
            return left and right

'''
# Not working solution
def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        bool = True
        queue = [root]
        while queue:
            curr = queue.pop(0)
            
            if curr.left:
                queue.append(curr.left)
                bool = curr.left.val < curr.val
                if not bool:
                    return False
            
            if curr.right:
                queue.append(curr.right)
                bool = curr.right.val > curr.val
                if not bool:
                    return False
        
        return bool
'''