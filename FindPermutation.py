# Array
# https://www.interviewbit.com/problems/find-permutation/

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        res = []
        n = 1
        stack = []
        for char in A:
            if char == "D":
                stack.append(n)
            if char == "I":
                stack.append(n)
                while stack:
                    res.append(stack.pop())
            n += 1
        stack.append(n)

        while stack:
            res.append(stack.pop())
        return res


inpA = "ID"
inpB = 3
out = Solution().findPerm(inpA, inpB)
print(out)

'''
D: small, I: big
4
1 2 3 4

IDI [1, 3, 2, 4], [1 4 3]
IDD
DII
DID

nD, mI
m+n = N

1 2 3 4 ...... N
   [nD]     [mI]
'''
