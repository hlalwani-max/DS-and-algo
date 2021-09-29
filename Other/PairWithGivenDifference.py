'''
STatus- Not Working
Two pointer- https://www.interviewbit.com/problems/pair-with-given-difference/

Given an one-dimensional unsorted array A containing N integers.
You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
Return 1 if any such pair exists else return 0.

Problem Constraints
1 <= N <= 105
-103 <= A[i] <= 103
-105 <= B <= 105

Input Format
First argument is an integer array A of size N.
Second argument is an integer B.

Output Format
Return 1 if any such pair exists else return 0.

Example Input
Input 1:
 A = [5, 10, 3, 2, 50, 80]
 B = 78

Input 2:
 A = [-10, 20]
 B = 30

Example Output
Output 1:
 1

Output 2:
 1

Example Explanation
Explanation 1:
 Pair (80, 2) gives a difference of 78.

Explanation 2:
 Pair (20, -10) gives a difference of 30 i.e 20 - (-10) => 20 + 10 => 30
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # Idea- If difference is less than target, increasing j will increase the difference, else increase i to find the new difference forward. If equal return true.
    # TC - O(NlogN), SC- O(1)
    def solve(self, A, B):
        N = len(A)
        A.sort()

        i, j = 0, 1

        while i < N and j < N:
            diff = A[j] - A[i]
            if i != j and diff == B:
                return 1
            elif diff < B:
                j += 1
            else:
                i += 1
        return 0

    # not woking
    def solve1(self, A, B):
        N = len(A)
        A.sort()

        l, r = 0, N - 1

        while l < r:
            diff = A[r] - A[l]
            if diff == B:
                return 1
            if diff < B:
                l += 1
            else:
                r -= 1

        return 0

    # not working
    def solve2(self, A, B):
        N = len(A)
        A.sort()

        def binarySearch(arr, start, end, target):
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            return False

        for i in range(N):

            target = B + A[i]
            if binarySearch(A, i + 1, N - 1, target): return 1

        return 0


if __name__ == "__main__":
    arr, target = [5, 10, 3, 2, 50, 80], 78
    out = Solution().solve(arr, target)
    print("Result: ", True if out == 1 else False)
