class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        map = {}
        ans = 0
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
        for i in range(1, 27):
            map[alpha[i - 1]] = i
        print(map)

        i = len(A) - 1
        for char in A:
            ans += (map[char] * (26 ** i))
            i -= 1

        return ans


inp = "AAA"
out = Solution().titleToNumber(inp)
print(out)
