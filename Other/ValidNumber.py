'''
Status- Not solved (failing for test case "1.e1": Expected zero, returned 1)

String- https://www.interviewbit.com/problems/valid-number/

Validate if a given string is numeric.

Examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false

Return 0 / 1 ( 0 for false, 1 for true ) for this problem


Clarify the question using “See Expected Output”?
Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.

Is 0.1e10 valid?
Yes

-01.1e-10?
Yes

Hexadecimal numbers like 0xFF?
Not for the purpose of this problem

3. (. not followed by a digit)?
No

Can exponent have decimal numbers? 3e0.1?
Not for this problem.

Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.

How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.

How about integers preceded by 00 or 0? like 008?
Yes for this problem
'''


class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        n = len(A)
        i = 0
        sign, sofar, exponential, decimal = False, True, False, False
        if n == 0:
            return False

        sign_set = set(["+", "-"])
        numeric_set = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

        if A[0] == "+" or A[0] == "-":
            sign = True

        while i < len(A):
            if sign and i == 0:
                i += 1
                continue
            if not sofar:
                return 0
            if A[i] not in numeric_set and A[i] not in ["e", "."]:
                sofar = False
            if sign and A[i] in sign_set:
                sofar = False
            if exponential and A[i] == "e":
                sofar = False
            if A[i] == "e":
                exponential = True
            if exponential and A[i] == ".":
                sofar = False
            if decimal and A[i] == ".":
                sofar = False
            if A[i] == ".":
                decimal = True
            i += 1

        return 1


if __name__ == "__main__":
    str = "1u"
    out = Solution().isNumber(str)
    print(out)
