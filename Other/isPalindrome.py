# String- https://www.interviewbit.com/problems/palindrome-string/

class Solution:
    # @param A : string
    # @return an integer
    # TC- O(N)
    def isPalindrome(self, A):
        n = len(A)
        if not A:
            return 0
        if n == 0 or n == 1:
            return 1

        def check(val):
            if 48 <= ord(val.lower()) <= 57 or 97 <= ord(val.lower()) <= 122:
                return True
            else:
                return False

        l, r = 0, n - 1
        while l <= r:
            if check(A[l]) == False or A[l] == "":
                l += 1
                continue
            if check(A[r]) == False or A[r] == "":
                r -= 1
                continue
            if A[l].lower() != A[r].lower():
                return 0
            l, r = l + 1, r - 1
        return 1


inp = "race a car"
out = Solution().isPalindrome(inp)
print(out)
