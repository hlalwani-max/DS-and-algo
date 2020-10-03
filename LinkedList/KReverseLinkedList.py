'''
https://www.interviewbit.com/problems/k-reverse-linked-list/
microsoft, amazon
Concept- modified reverse linked list function


Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.

NOTE : The length of the list is divisible by K
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.
'''

from LinkedList import convertLToLL, printLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B == 1: return A
        cur = A
        dummy = ListNode(-1)
        prev = dummy

        while cur:
            cur, prev = self.reverse(cur, prev, B)

        return dummy.next

    # return and return new curr and new prev
    def reverse(self, h, prev, K):
        N = 0
        curr = h
        org_h = h
        prevv = None

        # reverse linked list logic
        while N < K:
            N += 1
            tmp = curr.next
            curr.next = prevv
            prevv = curr
            curr = tmp

        prev.next = prevv
        org_h.next = curr

        return curr, org_h


if __name__ == "__main__":
    arr, K = [1,2,3,4,5,6], 2
    LL = convertLToLL(arr)
    out = Solution().reverseList(LL, K)
    print("K Reversed list:")
    printLL(out)
