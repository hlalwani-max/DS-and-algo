class Solution:
    # Time Complexity - O(N^2 * length of binary)
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        lA = len(A)

        if lA == 1:
            return 0

        perm = []
        for i in range(lA):
            for j in range(lA):
                perm.append([A[i], A[j]])
        print(perm)
        for i, pair in enumerate(perm):
            perm[i] = self.getdifference(self.getbinary(pair[0]), self.getbinary(pair[1]))

        print(perm)
        return sum(perm)

    def getdifference(self, str1, str2):
        diff = 0
        l1, l2 = len(str1), len(str2)

        if l1 > l2:
            pad = "0" * (l1 - l2)
            str2 = pad + str2
        elif l2 > l1:
            pad = "0" * (l2 - l1)
            str1 = pad + str1
        # print(str1, str2)

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff

    def getbinary(self, num):
        res = ""
        while num > 0:
            res = str(num % 2) + res
            num = num // 2
        return res


inp = [2, 6, 4]
out = Solution().hammingDistance(inp)
# tmp = Solution().getdifference(Solution().getbinary(2), Solution().getbinary(7))
# print(tmp)
print(out)
