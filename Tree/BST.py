class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:
    def addNode(self, root, data):
        if not root:
            return Node(data)
        else:
            if data <= root.data:
                root.left = self.addNode(root.left, data)
            else:
                root.right = self.addNode(root.right, data)
        return root

    def lookupNode(self,root,data):
        if not root:
            return False
        if root.data == data:
            return True
        else:
            if data <= root.data:
                return root.left
            else:
                return root.right
