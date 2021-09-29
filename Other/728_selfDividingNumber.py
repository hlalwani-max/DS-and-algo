class Solution:
    # def digits(self, n):
    #     digits = []
    #     for i in range(len(str(n))):
    #         digit = n % 10
    #         if digit == 0 :
    #             return False
    #         digits.append(digit)
    #         n = int(n / 10)
    #     # print(digits)
    #     return digits
    #
    # def numberCheck(self, num, digits):
    #     if not digits:
    #         return False
    #     for digit in set(digits):
    #         if digit == 0:
    #             return False
    #         if (num % digit != 0):
    #             return False
    #     return True


    def numberCheck(self, num):
        n = num
        while num!=0:
            digit = num % 10
            if digit == 0:
                return False
            if n % digit !=0:
                return False
            num = int(num/10)
        return True


    def selfDividingNumbers(self, left: int, right: int):
        res = []
        for i in range(left, right + 1):
            if self.numberCheck(i):
                res.append(i)
        return res

print(Solution().selfDividingNumbers(21,22))
