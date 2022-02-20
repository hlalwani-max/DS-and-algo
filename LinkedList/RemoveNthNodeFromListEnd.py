'''
https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
HCL Amazon
concept- simple iteration over LL.

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
'''

from LinkedList import convertLToLL, printLL


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        length = 0
        cur = A

        # calculate length
        while cur:
            length += 1
            cur = cur.next

        prev = None
        cur = A
        target = length - B + 1

        # if first element to delete, or condition B > length
        if target == 1 or B > length:
            return A.next

        # if element found at target index, skip the element by changing prev.next to next of element to skip.
        start = 0
        while cur:
            start += 1
            if start == target:
                prev.next = cur.next

            prev = cur
            cur = cur.next

        return A


if __name__ == "__main__":
    arr, target = [1, 2, 3, 4], 100
    LL = convertLToLL(arr)
    out = Solution().removeNthFromEnd(LL, target)
    print("New list after deleting {}th node from the end:".format(target))
    printLL(out)
