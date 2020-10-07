'''
https://www.interviewbit.com/problems/reorder-list/
Amazon Microsoft
Concept- reversal

Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

from LinkedList import printLL, convertLToLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    # Idea- Reverse other half of the list and merge
    # TC- O(N + N/2), SC - O(1)
    def reorderList(self, A):
        # initial condition check
        if not A or not A.next:
            return A

        cur = A

        # find length
        N = 0
        while cur:
            N += 1
            cur = cur.next

        # find mid
        mid = A
        for i in range(N // 2):
            mid = mid.next

        # split list - [start to mid], [mid+1 to end]
        firstHead = A
        secondHead = mid.next
        mid.next = None

        # reverse second list [mid+1 to end].
        prev = None
        while secondHead:
            nextNode = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = nextNode

        secondHead = prev

        #     merge two list
        while secondHead:  # since length of second length always be less than first
            nextFirst = firstHead.next
            nextSecond = secondHead.next

            firstHead.next = secondHead
            secondHead.next = nextFirst

            firstHead = nextFirst
            secondHead = nextSecond

        return A

    # TC- O(N^2), SC- O(N)
    def reorderList1(self, A):
        # initial check
        if not A or not A.next:
            return A

        cur = A

        while cur:
            nextNode = cur.next

            # get last node
            lastNode = cur.next
            prevLastNode = cur
            while lastNode and lastNode.next:
                prevLastNode = lastNode
                lastNode = lastNode.next

            # for 1,2,3,4 -> 1,4,2,3, while cur = 3 and preLastNode = 3, not need to go further.
            if prevLastNode == cur:
                return A

            # set prev of last node to none, and modify pointers.
            if lastNode:
                prevLastNode.next = None
                cur.next = lastNode
                lastNode.next = nextNode
            else:
                prevLastNode.next = None

            cur = nextNode

        return A


if __name__ == "__main__":
    l = [1, 2, 3, 4]
    LL = convertLToLL(l)
    out = Solution().reorderList(LL)
    print("Reordered List:")
    printLL(out)
