'''
Generate a tree.
'''

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)

