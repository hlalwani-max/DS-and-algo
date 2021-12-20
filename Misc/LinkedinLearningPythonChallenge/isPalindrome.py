import re

class Solution:
    def isPalindrome(self, str):
        forward = ''.join(re.findall('[a-z]+', str.lower()))
        backward = forward[::-1]
        return forward == backward

pal_bool = Solution().isPalindrome("I'm Mi")
print(pal_bool)