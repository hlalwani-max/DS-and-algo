'''
https://www.interviewbit.com/problems/rotate-list/
Amazon
Concept - Iteration: finding newHead and newTail and modifying list to accommodate them into our linked list.

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    # TC- O(N), SC- O(1)
    def rotateRight(self, A, B):
        N = 0

        # finding length of linked list
        cur = A
        while cur:
            N += 1
            cur = cur.next

        # remainder of B.
        B = B % N

        # corner cases
        if B == 0 or N < 2:
            return A
        else:
            # finding new head and new tail.
            i = 0
            newHead, newTail = None, None
            cur, prev = A, None
            target = N - B + 1
            while cur:
                i += 1
                if i == target:
                    newTail = prev
                    newHead = cur

                prev = cur
                cur = cur.next

        # modifying new linked list according to new head and tail below.
        # prev is last element of the list. (from 'else' while loop above). Point original last node to original head.
        if prev: prev.next = A
        A = newHead
        newTail.next = None

        return A


if __name__ == "__main__":
    arr, K = [1, 2, 3, 4, 5], 2
    LL = convertLToLL(arr)
    out = Solution().rotateRight(LL, K)
    print("New list with adjacent swapped pairs:")
    printLL(out)
