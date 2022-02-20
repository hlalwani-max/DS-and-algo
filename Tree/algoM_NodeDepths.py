from collections import deque

# TC- O(N), SC- O()
def nodeDepths(root):
    return nodeDepthsHelper(root, 0)


def nodeDepthsHelper(root, depth):
    if not root:
        return 0
    return depth + nodeDepthsHelper(root.left, depth + 1) + nodeDepthsHelper(root.right, depth + 1)


def nodeDepths1(root):
    # Write your code here.
    totalSum = 0
    Q = deque()
    Q.append([root, 0])

    while Q:
        currentNode = Q.popleft()
        totalSum += currentNode[1]

        if currentNode[0].left:
            Q.append([currentNode[0].left, currentNode[1] + 1])
        if currentNode[0].right:
            Q.append([currentNode[0].right, currentNode[1] + 1])

    return totalSum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)

totalDepth = nodeDepths(root)
print(totalDepth)
