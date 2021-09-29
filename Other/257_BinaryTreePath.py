# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = []
    backtrack = []

    def binaryTreePaths(self, root):
        self.res = []
        self.backtrack = []
        self.res = self.helper(root)
        return self.res

    def helper(self, root):
        if root:
            self.backtrack.append(root.val)

            if root.left == None and root.right == None:
                strr = ""
                l = len(self.backtrack)
                for i in range(l):
                    if i == l - 1:
                        strr += str(self.backtrack[i])
                    else:
                        strr += str(self.backtrack[i]) + "->"

                self.res.append(strr)
                # if (len(self.backtrack) != 0):
                #     self.backtrack.pop()

            self.helper(root.left)
            self.helper(root.right)
            if (len(self.backtrack) != 0):
                self.backtrack.pop()

        return self.res