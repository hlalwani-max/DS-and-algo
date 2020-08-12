# Array- Noble Integer
# https://www.interviewbit.com/problems/noble-integer/


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = len(A)
        A.sort()
        for i in range(l):
            p = A[i]

            # skiping same value elements
            if i + 1 < l and A[i + 1] == p:
                continue

            # count of elements with greater value
            count = l - i - 1

            if p == count:
                return 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    inp = [3, 2, 1, 3]
    print("Input: ", inp)
    ans = sol.solve(inp)
    print("Output: ", ans)
