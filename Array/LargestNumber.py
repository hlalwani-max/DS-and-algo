'''
https://www.interviewbit.com/problems/largest-number/
Amazon Goldman Sachs Microsoft
[Hard] Concept- sorting (modify comparator)

Given a list of non negative integers, arrange them such that they form the largest number.

For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
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
    arr = [3, 30, 34, 5, 9]
    ans = sol.largestNumber(arr)
    print("Largest Number possible is {}.".format(ans))
