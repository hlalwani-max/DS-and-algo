'''
https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/
Microsoft, Amazon
Concept- Iteration (use dummy pointer)

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

from LinkedList import convertLToLL, printLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    # TC - O(N), SC- O(1)
    def swapPairs(self, A):
        # sanity check: if no or one element.
        if not A or A.next is None:
            return A

        cur = A
        dummy = ListNode(-1)
        prev = dummy

        while cur and cur.next:
            h, t = cur, cur.next

            # store next node for swap to continue iteration to linked list.
            nextNode = t.next

            # modify pointers
            prev.next = t
            t.next = h
            h.next = nextNode

            # change prev and current
            prev = cur
            cur = nextNode

        return dummy.next


if __name__ == "__main__":
    arr = [1]
    LL = convertLToLL(arr)
    out = Solution().swapPairs(LL)
    print("New list with adjacent swapped pairs:")
    printLL(out)
