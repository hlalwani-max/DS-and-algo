'''
Math theories-
1. (A x B) % M = ( (A % M) x (B % M) ) % M
2. -A % M ≡ (M-A) % M
'''
#Math- https://www.interviewbit.com/problems/implement-power-function/

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, x, n, d):

        return self.helper(x, n, d)

    def helper(self, x, n, d):
        if x == 0 or x == 1:
            return x % d

        if n == 0:
            return 1 % d

        res = self.helper(x, n // 2, d)
        if n % 2 == 0:
            return (res % d * res % d) % d
        else:
            if res < 0:
                return (x % d + (res % d) * (res % d)) % d
            else:
                if x > 0:
                    return (x * (res % d) * (res % d)) % d
                else:
                    return (((x - d) % d) * (res % d) * (res % d)) % d
