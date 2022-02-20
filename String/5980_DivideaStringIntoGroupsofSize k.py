class Solution:
    def divideString(self, s, k, fill):
        count = 0
        ans = []
        curr = ''
        for i in range(len(s)):
            curr += s[i]
            count += 1
            if count == k:
                ans.append(curr)
                count = 0
                curr = ''

        if len(curr) > 0:
            diff = k - len(curr)
            for i in range(diff):
                curr += fill

            ans.append(curr)

        return ans


inp = ["abcdefghijk",
       3,
       "x"]
print(Solution().divideString(inp[0], inp[1], inp[2]))
