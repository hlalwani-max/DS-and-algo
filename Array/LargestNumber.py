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
    # @param A : tuple of integers
    # @return a string
    # Idea- make your own comparator for sorting that chooses whichever is bigger of two sub strings.
    # TC- O(NlogN), SC- O(N)
    def largestNumber(self, A):
        res = ""
        l = len(A)

        if l == 0:
            return res

        # Sort Array in decreasing order
        strArr = [str(x) for x in A]
        # modified comparator function key. Using functools
        strArr = sorted(strArr, key=functools.cmp_to_key(self.myComp), reverse=True)

        ans = "".join(strArr)

        # sanity check, if 0 encountered in the beginning.
        if ans[0] == "0":
            return ans[0]

        return ans

    # new comparator function key- (greedy approach) look for which of two of adding is greater, return that.
    # Here, to pick t1, return '1', else to pick t2, return '-1'.
    def myComp(self, x, y):
        t1 = x + y
        t2 = y + x

        if t1 > t2:
            return 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 30, 34, 5, 9]
    ans = sol.largestNumber(arr)
    print("Largest Number possible is {}.".format(ans))
