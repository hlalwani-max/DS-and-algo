class Solution(object):
    # primes = []

    def findPrimeFactors(self, n):
        primes = []
        div = 2

        while (div <= n):
            if n % div == 0:
                primes.append(div)
                n = int(n / div)
            else:
                div += 1
        return primes

    # ineficient solution
    # def isPrime(self, n):
    #     count = 0
    #     for i in range(2, n+1):
    #         if count >1:
    #             return False
    #         if n % i==0:
    #             count+=1
    #
    #     return True
    #
    #
    # def findPrimeFactors(self, n):
    #     if n==1:
    #         return self.primes
    #     for i in range(2,n+1):
    #         if n%i == 0:
    #             if self.isPrime(i):
    #                 self.primes.append(i)
    #                 self.findPrimeFactors(int(n/i))
    #                 break
    #     return self.primes


primes = Solution().findPrimeFactors(630)
print(primes)
