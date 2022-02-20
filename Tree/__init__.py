from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __int__(self):
        self.data = None
        self.left = None
        self.right = None


def getTreeUsingLevelOrder(arr):
    N = len(arr)

    if N == 0:
        return TreeNode()
    else:
        root = TreeNode(arr[0])
        Q = deque([root, 0])

        while Q:
            curr = Q.popleft()
            node, index = curr[0], curr[1]

            left_child_index = 2 * index + 1
            if left_child_index < N:
                left_child = TreeNode(arr[left_child_index])
                if left_child:
                    node.left = left_child
                    Q.appendleft([left_child, left_child_index])

            right_child_index = 2 * index + 2
            if right_child_index < N:
                right_child = TreeNode(arr[right_child_index])
                if right_child:
                    node.right = right_child
                    Q.appendleft([right_child, 2 * index + 2])

        return root
