'''
https://www.interviewbit.com/problems/noble-integer/
NA
Concept- sorting

Given an integer array A, find if an integer p exists in the array such that the number of integers
greater than p in the array equals to p.

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is found else return -1.

Example Input
Input 1:
 A = [3, 2, 1, 3]
Input 2:
 A = [1, 1, 3, 3]

Example Output
Output 1:
 1
Output 2:
 -1
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    # Idea- sort list, finding number of elements greater than the element 'p' becomes easy.
    # TC- O(NlogN), SC- O(1)
    def solve(self, A):
        A.sort()
        N = len(A)

        for i in range(N):
            if i + 1 < N - 1 and A[i] == A[i + 1]:
                continue

            count = self.getcount(length=N, ind=i)
            p = A[i]
            if count == p:
                return 1

        return -1

    def getcount(self, length, ind):
        return length - ind - 1


if __name__ == "__main__":
    arr = [3, 2, 1, 4]
    out = Solution().solve(arr)
    print("Noble integer exists." if out == 1 else "Noble integer doesn't exists.")
