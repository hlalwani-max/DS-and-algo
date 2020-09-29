'''
Two pointers- https://www.interviewbit.com/problems/counting-triangles/

You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:
You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.
Return answer modulo 109 + 7.

For example,
A = [1, 1, 1, 2, 2]

Return: 4
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        N = len(A)
        mod = 10 ** 9 + 7
        ans = 0

        for i in range(N - 2):
            a = A[i]

            j, k = i + 1, i + 2

            while j != k and j < N and k < N:
                b, c = A[j], A[k]
                if a + b > c:
                    ans += (k - j)
                    k += 1
                else:
                    j += 1

        return ans % mod


if __name__ == "__main__":
    arr = [4, 6, 13, 16, 20, 3, 1, 12]
    out = Solution().nTriang(arr)
    print("{} traingles can be formed of given combination.".format(out))
