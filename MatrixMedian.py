# Not finished!!

class Solution:
    def binarySearchCount(arr, n, key):

        left = 0
        right = n - 1

        count = 0

        while (left <= right):
            mid = int((right + left) / 2)

            # Check if middle element is
            # less than or equal to key
            if (arr[mid] <= key):

                # At least (mid + 1) elements are there
                # whose values are less than
                # or equal to key
                count = mid + 1
                left = mid + 1

            # If key is smaller, ignore right half
            else:
                right = mid - 1

            return count

    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        r, c = len(A), len(A[0])
        if r == 1:
            return (A[c//2])
        else:
            minA, maxA = A[0][0], 0
        for i in range(r):
            if A[i][0] < minA:
                minA = A[i][0]
            if A[i][c-1] < maxA:
                maxA = A[i][c-1]

        desired = (r * c) // 2 + 1


        while minA < maxA:
            mid = minA + (maxA - minA) // 2

            count = 0
            for i in range(r):
                count+= self.binarySearch(A[i], c, mid)

            if count == desired:
                return A[mid]
            elif count < desired:
                minA = mid + 1
            else:
                maxA = mid



