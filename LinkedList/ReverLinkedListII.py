'''
https://www.interviewbit.com/problems/reverse-link-list-ii/
Facebook Microsoft Amazon
Concept- linked list reversal

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.
'''

from LinkedList import printLL, convertLToLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    # TC- O(N), SC- O(1)
    def reverseBetween(self, A, B, C):
        if B == C:
            return A

        cur = A
        # add dummy to the list.
        dummy = ListNode(-1)
        dummy.next = cur
        prev = dummy

        count = 0
        while cur:
            count += 1

            # send head to begin reverseLL when start is found
            if count == B:
                self.reverseLL(head=cur, prevv=prev, start=B, upto=C)
                return dummy.next

            prev = cur
            cur = cur.next

        return dummy.next

    def reverseLL(self, head, prevv, start, upto):
        curNode = head
        nextNode = None
        prevNode = None

        # reversal happens inside
        c = start
        while c <= upto and curNode:
            c += 1
            nextNode = curNode.next

            curNode.next = prevNode

            prevNode = curNode
            curNode = nextNode

        endNode = prevNode

        # binding the reversal.
        prevv.next = endNode
        head.next = nextNode


if __name__ == "__main__":
    l, start, end = [1, 2, 3, 4, 5, 6], 2, 5
    LL = convertLToLL(l)
    out = Solution().reverseBetween(LL, start, end)
    print("Reversed list form index {} to {} is:".format(start, end))
    printLL(out)
