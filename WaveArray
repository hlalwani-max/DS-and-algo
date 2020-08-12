# Array- Wave Array
# https://www.interviewbit.com/problems/wave-array/


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        l = len(A)

        if l == 1:
            return A

        A = sorted(A)

        for i in range(0, l-1, 2):
            A[i], A[i+1] = A[i+1], A[i]

        return A


if __name__ == "__main__":
    sol = Solution()
    inp = [5, 1, 3, 2, 4]
    print("Input: ", inp)
    ans = sol.wave(inp)
    print("Output: ", ans)
