class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Print Linked List
def printLL(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next


# Take list and generate linked list
def convertLToLL(arr):
    N = len(arr)
    if N == 0: return ListNode()

    head = ListNode(arr[0])
    curr = head

    for i in range(1, N):
        node = ListNode(arr[i])
        curr.next = node
        curr = curr.next

    return head
