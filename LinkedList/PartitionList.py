'''
https://www.interviewbit.com/problems/partition-list/
Microsoft
Concept- Iteration

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
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
    # @return the head node in the  linked list
    # TC- O(N), SC- O(N)
    # Idea - make seperate smaller value list and greater value linked list and bind them. Order retained.
    def partition(self, A, B):
        cur = A
        small, large = None, None
        headS, headL = None, None

        while cur:
            temp = ListNode(cur.val)

            if cur.val < B:
                if not small:
                    headS = temp
                    small = temp
                else:
                    small.next = temp
                    small = small.next

            else:
                if not large:
                    headL = temp
                    large = temp
                else:
                    large.next = temp
                    large = large.next

            cur = cur.next

        if headS:
            small.next = headL
            return headS
        else:
            return headL

    # TC- O(N), SC- O(N)
    # Idea - save smaller value and greater value in seperate list in order and make a new list out of it.
    # Bind the list. Order retained.
    def partition1(self, A, B):
        smallEle = []
        greaterEle = []
        cur = A
        dummy = ListNode(-1)
        prev = dummy

        while cur:
            if cur.val < B:
                smallEle.append(cur.val)
            else:
                greaterEle.append(cur.val)
            cur = cur.next

        for item in smallEle:
            newNode = ListNode(item)
            prev.next = newNode
            prev = newNode

        for item in greaterEle:
            newNode = ListNode(item)
            prev.next = newNode
            prev = newNode

        return dummy.next


if __name__ == "__main__":
    l, value = [1, 4, 3, 2, 5, 6], 3
    LL = convertLToLL(l)
    out = Solution().partition(LL, value)
    print("Partition list for value {}:".format(value))
    printLL(out)
