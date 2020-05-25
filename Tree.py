class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = Node(1)
root.right = Node(2)
root.right.left = Node(3)

