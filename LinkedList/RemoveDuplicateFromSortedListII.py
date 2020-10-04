'''
Linked List- https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list-ii/
Concept- interation (use prev pointer)
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
    # checkout source- https://www.youtube.com/watch?v=rcKmKBmC2NY
    def deleteDuplicates(self, A):
        prev = None
        cur = A
        duplicate = False

        while cur:
            tmp = cur

            # find next non-duplicate
            while tmp.next and tmp.next.val == cur.val:
                duplicate = True
                tmp = tmp.next

            # change pointers if duplicate found, handle corner cases.
            if duplicate:
                duplicate = False
                if prev:
                    prev.next = tmp.next
                    cur = prev.next
                    continue
                # if duplicate in the begining
                else:
                    A = tmp.next
                    cur = A
                    continue

            prev = cur
            cur = cur.next

        if not prev:
            return None

        return A


if __name__ == "__main__":
    arr = [2, 1, 1, 1]
    LL = convertLToLL(arr)
    out = Solution().deleteDuplicates(LL)
    print("New list with removing values with duplicates is:")
    printLL(out)
