class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        # map = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYA"))
        # print(map)
        res = ""
        while A:
            res = chr((A - 1) % 26 + 65) + res
            A = (A - 1) // 26

        return res

    def convertToTitl1(self, A):
        map = dict(zip(range(1, 27), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        print(map)
        ans = ""
        divident = A
        power = 9
        while power >= 0:
            rem = divident % (26 ** power)
            div = divident // (26 ** power)
            if div == 0:
                power -= 1
                continue
            else:
                ans += map[div]
                divident = rem
                power -= 1
        return ans


inp = 943566
out = Solution().convertToTitle(inp)
print(out)
