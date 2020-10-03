'''
https://www.interviewbit.com/problems/merge-two-sorted-lists/
Microsoft Yahoo Amazon

concept- iteration (use dummy)
'''

from LinkedList import convertLToLL, printLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        cur1, cur2 = A, B
        dummy = ListNode(-1)
        cur = dummy

        # choose minimum of two and put in current
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        # if remaining of two list left, bind it.
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2

        return dummy.next

    # my solution not working. Fix it later. Cornor case- when prev = None
    def mergeTwoLists1(self, A, B):
        cur1, cur2 = A, B
        prev1 = None

        while cur1 and cur2:
            if cur1.val > cur2.val:
                # insert node in the middle
                newNode = ListNode(cur2.val)
                tmp = prev1.next
                prev1.next = newNode
                newNode.next = tmp

                cur2 = cur2.next
                cur1 = cur1.next.next
            else:
                prev1 = cur1
                cur1 = cur1.next

        if cur2:
            prev1.next = cur2

        return A


if __name__ == "__main__":
    arr1, arr2 = [1, 3, 5], [2, 4, 6]
    LL1, LL2 = convertLToLL(arr1), convertLToLL(arr2)
    out = Solution().mergeTwoLists(LL1, LL2)
    print("Merged Linked List:")
    printLL(out)
