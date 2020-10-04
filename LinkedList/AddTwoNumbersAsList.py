'''
https://www.interviewbit.com/problems/add-two-numbers-as-lists/
Amazon Qualcomm Microsoft Facebook
Concept- Iteration - calculate sum digits and bind them to result list. Take care of corner cases.

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''

from LinkedList import printLL, convertLToLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    # TC - O(N), SC- O(N)
    def addTwoNumbers(self, A, B):
        carry = 0

        # new sum list to return.
        dummy = ListNode(-1)
        prev = dummy

        # until equal length of list, sum.
        while A and B:
            s = A.val + B.val + carry
            if carry == 1: carry = 0

            # if sum is greater than one digit, send it in carry.
            if s > 9:
                carry = 1
                s = s % 10

            # sum digit, create new node and bind it to new list.
            newNode = ListNode(s)
            prev.next = newNode

            prev = newNode
            A = A.next
            B = B.next

        # for left of A or B, repeat the same process.
        while A:
            s = A.val + carry
            if carry == 1: carry = 0

            if s > 9:
                carry = 1
                s = s - 10
            newNode = ListNode(s)
            prev.next = newNode

            prev = newNode
            A = A.next

        while B:
            s = B.val + carry
            if carry == 1: carry = 0

            if s > 9:
                carry = 1
                s = s - 10
            newNode = ListNode(s)
            prev.next = newNode

            prev = newNode
            B = B.next

        # if carry left away...
        if carry == 1:
            newNode = ListNode(carry)
            prev.next = newNode

        return dummy.next


if __name__ == "__main__":
    l1, l2 = [0], [1, 0, 1]
    LL1, LL2 = convertLToLL(l1), convertLToLL(l2)
    out = Solution().addTwoNumbers(LL1, LL2)
    print("(List) Sum of two linked list is:")
    printLL(out)
