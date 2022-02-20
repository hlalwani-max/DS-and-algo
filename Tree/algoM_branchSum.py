# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# TC- O(N), SC- O(N)
def branchSums(root):
    res = []
    branchSumsHelper(root, 0, res)
    return res


def branchSumsHelper(root, sum, result):
    if not root:
        return

    sum += root.value
    if not root.left and not root.right:
        result.append(sum)

    branchSumsHelper(root.left, sum, result)
    branchSumsHelper(root.right, sum, result)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right.left = BinaryTree(10)
res = branchSums(root)
print(res)
