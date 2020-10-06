'''
https://www.interviewbit.com/problems/list-cycle/
Amazon Microsoft NetApp
Concept- Floyd cycle detection in linked list (using slow and fast pointer). How to find the cycle's start in the algorithm? (for later)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input :

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    # Idea- using hashing. Store nodes that are visited
    # TC- O(N), SC- O(N)
    def detectCycle(self, A):
        s = set()
        while A:
            if A in s:
                return A
            s.add(A)
            A = A.next

        return None

    # My naive solution: TC - O(N), SC- O(N)
    # Idea - change visited data type to tuple and maintain visited.
    def detectCycle1(self, A):
        while A:
            if type(A.val) is tuple and A.val[1]:
                A.val = A.val[0]
                return A

            A.val = (A.val, True)

            A = A.next

        return None


if __name__ == "__main__":
    # build test linkedlist
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next

    out = Solution().detectCycle(head)
    print("Cycle begins at node {}.".format(out.val))
