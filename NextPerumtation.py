# Array
# https://www.interviewbit.com/problems/next-permutation/
# video explanation - https://www.youtube.com/watch?v=PYXl_yY-rms

'''

Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

Input 3:
    A = [1, 1, 5]

Output 3:
    [1, 5, 1]

Input 4:
    A = [20, 50, 113]

Output 4:
    [20, 113, 50]

Your Input: 1 1 5 4 6
Expected output is 1 1 5 6 4

Your Input: 1 1 5 4
Expected output is 1 4 1 5

[1 1 5 4 0] <- find k such that k<k+1 element
replace with second smallest (l) to the right split
swap l and k
reverse right split



OR
(more time complexity)
find k starting from left such that k+1>k, split at k
find smallest element of the right k,
replace l and k
sort right split

'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        lenA = len(A)
        k = lenA - 2
        while k > -1 and A[k] > A[k + 1]:
            k -= 1

        # k is conflict
        # if no conflict found
        if k == -1:
            self.reverse(A, 0, lenA - 1)
            return A

        # find closest minimum to k in right split
        min = A[k + 1]
        l = k + 1
        min_ind = k + 1
        while l < lenA:
            if A[l] < min and A[l] > A[k]:
                min, min_ind = A[l], l

            l += 1

        # swap k an next min
        tmp = A[min_ind]
        A[min_ind] = A[k]
        A[k] = tmp

        start = k + 1
        end = lenA - 1
        self.reverse(A, start, end)

        return A

    def reverse(self, arr, start, end):
        while start < end:
            tmp = arr[start]
            arr[start] = arr[end]
            arr[end] = tmp
            start, end = start + 1, end - 1


inp = [5, 4, 3, 2]
out = Solution().nextPermutation(inp)
print(out)
