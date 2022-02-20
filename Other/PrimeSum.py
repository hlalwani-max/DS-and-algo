# Math - Find two prime whose sum is equal to the input integer
# https://www.interviewbit.com/problems/prime-sum/

import math


class Solution:
    # Space complexity - O(N)
    # Finding Prime numbers - Sieve of Eratosthenes - https://www.youtube.com/watch?v=eKp56OLhoQs&feature=emb_err_woyt
    # @param A : integer
    # @return a list of integers
    def primesum1(self, A):
        primes = [[i, True] for i in range(0, A + 1)]
        primes[0][1], primes[1][1] = False, False
        ans = [None, None]

        # sqrt_A = int(math.sqrt(A))
        for i in range(A + 1):
            curr, bool = primes[i][0], primes[i][1]

            if not bool:
                continue

            else:
                # we want to start for number greater 2
                j = 2
                while curr * j < A + 1:
                    primes[curr * j][1] = 0
                    j += 1

        primes = [primes[i][0] for i in range(A + 1) if primes[i][1] is True]
        # print(primes)
        l = 0
        r = len(primes) - 1

        while l <= r:
            if primes[l] + primes[r] == A:
                ans[0], ans[1] = primes[l], primes[r]
                return ans
            elif primes[l] + primes[r] < A:
                l += 1
            else:
                r -= 1

    # Space- O(1), Time- O(N/2+sqrt(N))
    def primesum(self, A):

        for i in range(2, A // 2 + 1):
            if self.isPrime(i) and self.isPrime(A - i): return [i, A - i]

    def isPrime(self, num):
        if num == 2:
            return True
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False

        return True


inp = 10
out = Solution().primesum(inp)
print(out)
