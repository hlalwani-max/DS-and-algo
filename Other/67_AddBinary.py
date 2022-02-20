class Solution:
    # def strBinaryToDeci(self, str):
    #     # sum(str() for item in str)
    #     num = 0
    #     for i in range(len(str)):
    #         num += int(str[len(str) - i - 1]) * (2**i)
    #     return num


    def addBinary(self, a: str, b: str) -> str:
        # num1 = self.strBinaryToDeci(a)
        # num2 = self.strBinaryToDeci(b)

        # return self.intToBinary(num1 + num2)
        res = ""
        # stack = []
        carry = 0
        len_b = len(b)
        len_a = len(a)
        MAX = max(len_a,len_b)
        MIN = min(len_a, len_b)
        j = MIN - 1

        if len_a > len_b:
            aa = a
            bb = b
        else:
            aa = b
            bb = a
        #
        for i in range(MAX-1, -1, -1):
            # print("stack\n", stack)

            # if i >= MIN - 1:
            if j>=0:
                summ = (int(aa[i]) + int(bb[j]) + carry)
                # print("sum=",summ)
                if summ == 0:
                    carry = 0
                    # stack.append(0)
                    res = "0" + res
                elif summ == 1:
                    carry = 0
                    res = "1" + res
                elif summ == 2:
                    carry = 1
                    res = "0" + res
                else:
                    carry = 1
                    res = "1" + res
                j-=1
            # print(stack)
            else:
                    summ = int(aa[i]) + carry
                    if summ == 0:
                        carry = 0
                        res = "0" + res
                    elif summ == 1:
                        carry = 0
                        res = "1" + res
                    else:
                        carry = 1
                        res = "0" + res


        if carry == 1:
            res = "1" + res

        if res == "":
            return "0"

        return res

    # def intToBinary(self, num):
    #     stack = []
    #     # for i in range(len(str(num))):
    #     while num!=0:
    #         stack.append(num % 2)
    #         num = int(num / 2)
    #
    #     binary_str = ""
    #     if len(stack) == 0:
    #         return "0"
    #     while stack:
    #         binary_str+=str(stack.pop())
    #
    #     return binary_str

s1 = "100"
s2 = "110010"

# s1 = "1"
# s2 = "111"
print("ans=",Solution().addBinary(s1, s2))