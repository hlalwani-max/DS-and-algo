class Node:
    def __init__(self, val):
        if val == "null":
            self.val = None
        else:
            self.val = val
        self.left = None
        self.right = None


class BT:
    def levelOrderTraversal(self, list, root, i, n):
        if i < n:
            root = Node(list[i])
            # confused why root.left in argument of recursion
            root.left = self.levelOrderTraversal(list, root.left, 2 * i + 1, n)
            root.right = self.levelOrderTraversal(list, root.right, 2 * i + 2, n)
        return root

    def printPreOrderTraversal(self, root):
        if root:
            print(root.val)
            self.printPreOrderTraversal(root.left)
            self.printPreOrderTraversal(root.right)

    def listToBT(self, list):
        if len(list) == 0:
            return ValueError("List is empty")
        root = None
        i = 0
        n = len(list)
        root = self.levelOrderTraversal(list, list[0], 0, n)
        return root


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    binaryTree = BT()
    root = binaryTree.listToBT(list)
    binaryTree.printPreOrderTraversal(root)
