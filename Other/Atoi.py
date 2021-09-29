class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        n = len(A)
        if not A or n == 0:
            return 0

        INT_MIN = -2 ** 31
        # print(INT_MIN)
        INT_MAX = 2 ** 31 - 1

        minus_bool, ans_bool = False, True
        ans = ""

        r1, r2 = ord("0"), ord("9")

        i = 0
        while ans_bool and i < n:
            # print(ans)
            if i == 0 and A[0] == "-":
                minus_bool = True
                i += 1
                continue
            if i == 0 and A[0] == "+":
                i += 1
                continue

            if r1 <= ord(A[i]) <= r2:
                ans += A[i]

            else:
                if len(ans) == 0:
                    ans_bool = False
                else:
                    break
            i += 1

        if len(ans) == 0:
            return 0
        else:
            res = int(ans)

            if minus_bool:
                if -res < INT_MIN:
                    return INT_MIN
                return -res
            else:
                if res > INT_MAX:
                    return INT_MAX
                return res


inp = "-54332872018247709407 4 54"
out = Solution().atoi(inp)
print(out)

'''
IB Solution
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, s):
        s = s.strip() # strips all spaces on left and right
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        val, index = 0, 0
        if s[0] in ['+', '-']: index = 1
        while index < len(s) and s[index].isdigit():
            val = val*10 + ord(s[index]) - ord('0') # assumes there're no invalid chars in given string
            index += 1
        #return sign*val
        return max(-2**31, min(sign * val,2**31-1))
'''