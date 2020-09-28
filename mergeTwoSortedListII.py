'''
String- Merge two sorted list II: https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :
Input :
         A : [1 5 8]
         B : [6 9]
Modified A : [1 5 6 8 9]
'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # Trick - Start pointers with heads on both arrays, write min(head1, head2) into res array and increment head pointer whichever was picked. For remaining of elements, append them in order to result array
    # TC- O(M+N), SC- O(M+N)
    def merge(self, A, B):
        m, n = len(A), len(B)
        res = []

        i, j = 0, 0
        while i < m and j < n:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1

        if i == m and j < n:
            for i in range(j, n):
                res.append(B[j])
        elif j == n and i < m:
            for i in range(i, m):
                res.append(A[i])

        A = res

        return A


if __name__ == "__main__":
    arr1, arr2 = [-4, 3], [-2, -2]
    out = Solution().merge(arr1, arr2)
    print(out)
