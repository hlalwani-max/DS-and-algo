class Solution:
    def squareDigitsSum(self, num):
        sum = 0
        while int(num / 10) != 0:
            sum += (num % 10) ** 2
            num = int(num / 10)
        sum += (num % 10) ** 2
        return sum

    def isHappy(self, n):

        map = {}
        while n != 1:
            n = self.squareDigitsSum(n)
            print(n)
            if n in map:
                return False
            else:
                map[n] = 1
        return True

inp = 2
sol = Solution()
print(sol.isHappy(inp))