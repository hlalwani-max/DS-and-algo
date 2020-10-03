'''
Linked List- https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
Microsoft, Vmware
concept- simply iteration.

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

from LinkedList import convertLToLL, printLL


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    # source- https://www.youtube.com/watch?v=wIB5sg_Ulx4
    def deleteDuplicates(self, A):
        cur = A

        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return A

    # Another approach
    def deleteDuplicates1(self, A):
        cur = A
        found = False
        while cur:
            tmp = cur
            # iterate to the last occured same cur.
            while tmp.next and tmp.next.val == cur.val:
                found = True
                tmp = tmp.next

            if found:
                # change cur next to next of last occured same cur.
                cur.next = tmp.next
                found = False

            cur = cur.next

        return A


if __name__ == "__main__":
    arr = [1, 1, 1, 3]
    LL = convertLToLL(arr)
    out = Solution().deleteDuplicates(LL)
    print("New list with no duplicates is:")
    printLL(out)
