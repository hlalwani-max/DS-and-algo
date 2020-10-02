'''
Linked List - https://www.interviewbit.com/problems/palindrome-list/
Amazon, Microsoft

concepts- reverse, finding mid (speed pointers)
'''

from LinkedList import convertLToLL, printLL


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        # check if there is 0 or 1 element in the linked list
        if not A or not A.next:
            return 1

        slow, fast = A, A

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        p1, p2 = A, slow.next
        # updated head (p2) for reverse LL
        p2 = self.reverse(p2)

        # palindrome check
        while p2:
            if p1.val != p2.val:
                return 0
            p1, p2 = p1.next, p2.next

        return 1

    # reverse the linked list and return reversed LL head.
    def reverse(self, h):
        if not h:
            return None

        prev = None
        curr = h

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


if __name__ == "__main__":
    arr = [6, 3, 7,3,6]
    LL = convertLToLL(arr)
    out = Solution().lPalin(LL)
    print("Palindrome" if out == 1 else "Not palindrome")
