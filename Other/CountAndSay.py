# String- https://www.interviewbit.com/problems/count-and-say/


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A == 0:
            return ""
        ans = "1"
        i = 2

        def create(ans):
            s = str(ans)
            n = len(s)
            ans = ""
            i = 0

            while i < n:
                count = 1
                while i + 1 < n and s[i] == s[i + 1]:
                    count += 1
                    i = i + 1
                ans += (str(count) + str(s[i]))
                i += 1

            return ans

        while i <= A:
            ans = create(ans)
            i += 1

        return ans


inp = 2
out = Solution().countAndSay(inp)
print(out)
