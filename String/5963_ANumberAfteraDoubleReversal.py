'''
5963. A Number After a Double Reversal
Difficulty:Easy

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.


Constraints:
0 <= num <= 10^6
'''


'''
Idea - 
The only time the reversal would not be equal will be when you have zero(s) tailing the number since number is not 
negative or decimal.

'''
class Solution:
    def isSameAfterReversals(self, num):
        str_num = str(num)
        n = len(str_num)

        i = n - 1
        lzero_in_end = 0
        while (i >= 0):
            if str_num[i] == '0':
                lzero_in_end += 1
            else:
                break
            i -= 1

        if lzero_in_end == 0:
            return True
        #  true if one zero
        elif lzero_in_end == 1:
            if n == 1:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    num = 10
    out = Solution().isSameAfterReversals(num)
    print(out)
