'''
String: Power of 2 -  https://www.interviewbit.com/problems/power-of-2/

Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.

Input:
number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
Output:
return 1 if the number is a power of 2 else return 0

Example:
Input : 128
Output : 1
'''

import math


class Solution:
    # @param A : string
    # @return an integer
    # TC- O(N)
    def power(self, A):
        num = int(A)
        check = False
        while num % 2 == 0:
            check = True
            num = num // 2

        if check and num == 1:
            return 1
        return 0

    # IB Solution
    def power(self, A):
        num = int(A)
        if (num < 2): return 0
        if (math.ceil(math.log2(num)) == math.log2(num)): return 1
        return 0


if __name__ == "__main__":
    str = "1024"
    out = Solution().power(str)
    print("{} is 2 power {}".format(str, out))
