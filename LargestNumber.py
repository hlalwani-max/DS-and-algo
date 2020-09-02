# Array- Largest Number
# https://www.interviewbit.com/problems/largest-number/
import functools


class Solution:
    def myComp(self, x, y):
        t1 = x + y
        t2 = y + x

        if t1 > t2:
            return 1
        return -1

    # @param A : tuple of integers
    # @return a string

    def largestNumber(self, A):
        # A = map(str, A)
        # print(A)
        res = ""
        l = len(A)

        if l == 0:
            return res

        # Sort Array in decreasing order
        strArr = [str(x) for x in A]
        strArr = sorted(strArr, key=functools.cmp_to_key(self.myComp), reverse=True)

        ans = "".join(strArr)

        if ans[0] == "0":
            return ans[0]

        return ans


if __name__ == "__main__":
    sol = Solution()
    inp = [3, 34, 345, 5, 9, 99, 95]
    print("Input: ", inp)
    ans = sol.largestNumber(inp)
    print("Output: ", ans)
