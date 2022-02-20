'''
Status- inccomplete, copy linked list, break linked list and merge them.
https://www.interviewbit.com/problems/sort-list/
Google
Concept- sorting (merge sort concept)

Sort a linked list in O(n log n) time using constant space complexity.

Example :
Input : 1 -> 5 -> 4 -> 3
Returned list : 1 -> 3 -> 4 -> 5

Solution-
def mergeTwoLists(A, B):
    i = A; j = B
    #i is the pointer to the current node in A
    #j is the pointer to the current node in B
    first = None; last = None
    #first is the first node in the sorted list
    #last is the last node in the sorted list
    while i and j:
        #choose node with the minimum value, and update the current one
        if i.val<j.val:
            min_n = i; i = i.next
        else:
            min_n = j; j = j.next
        #update last and first
        if last is None: first = last = min_n
        else:
            last.next = min_n; last = min_n
    #extend the rest to the list
    while i:
        last.next = i; last = i; i = i.next
    while j:
        last.next = j; last = j; j = j.next
    last.next = None
    return first

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None or A.next is None: return A
        i = A; n = 0
        while i is not None:
            i = i.next; n+=1
        #now n = len(A)
        mid = A
        for t in range(n//2-1):
            mid = mid.next
        B = mid.next
        mid.next = None
        return mergeTwoLists(self.sortList(A), self.sortList(B))

'''

from LinkedList import printLL, convertLToLL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        l, r = 0, self.length(ll=A)
        self.helper(llist=A, left=l, right=r)
        return A

    def helper(self, llist, left, right):
        if left < right:
            # find mid.
            slow, fast = llist, llist
            while fast:
                slow = slow.next
                fast = fast.next.next

            mid = slow

            self.helper(llist, left, mid)
            self.helper(llist, mid + 1, right)
            self.merge(llist, left, mid, right)

    def length(self, ll):
        head = ll
        res = 0
        while head:
            res += 1
            head = head.next

        return res

    def merge(self, head, l, m, r):

        curr = head

        # split list into leftLL and rightLL

        i = l
        dummy = ListNode(-1)
        prev = dummy
        while i <= m - 1:
            prev.next = ListNode(curr.val)
            prev = curr
            curr = curr.next
            i += 1

        if prev: prev.next = None
        leftLL = dummy.next

        j = m.next
        dummy = ListNode(-1)
        prev = dummy
        while j <= r:
            prev.next = ListNode(curr.val)
            prev = curr
            curr = curr.next
            j += 1

        if prev: prev.next = None
        rightLL = dummy.next

        # sort and merge leftLL and rightLL into A.

        curr = head
        currL, currR = leftLL, rightLL
        while currL and currR:
            if currL.val < currR.val:
                curr.val = currL.val
                currL = currL.next
            else:
                curr.val = currR
                currR = currR.next
            curr = curr.next

        while currL:
            curr.val = currL.val
            currL = currL.next
            curr = curr.next

        while currR:
            curr.val = currR.val
            currR = currR.next
            curr = curr.next


if __name__ == "__main__":
    l = [1, 5, 4, 3]
    LL = convertLToLL(l)
    out = Solution().sortList(LL)
    print("Sorted List:")
    printLL(out)
