def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestValueinBstHelper(tree, target, tree.value)


def findClosestValueinBstHelper(root, target, closest):
    if not root:
        return closest
    if abs(target - root.value) < abs(target - closest):
        closest = root.value
    if target < root.value:
        return findClosestValueinBstHelper(root.left, target, closest)
    if target > root.value:
        return findClosestValueinBstHelper(root.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
