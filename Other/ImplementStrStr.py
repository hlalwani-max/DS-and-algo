# String (find substring index)

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, haystack, needle):
        N, H = len(needle), len(haystack)

        for i in range(H - N + 1):
            for j in range(N):
                if haystack[i + j] != needle[j]:
                    break

                if j == N - 1:
                    return i
        return -1


hay, needle = "bbbbbbbbab", "baba"
out = Solution().strStr(hay, needle)
print(out)
