class Solution:
    def reverseString2(self, s):
        l = len(s)
        for i in range(int(l/2)):
            temp = s[l-i-1]
            s[l - i - 1] = s[i]
            s[i] = temp
        print(s)

    # def recursion(self,s, l, r):
    #
    #
    #     while l<=r:
    #         self.recursion(s, l+1, r-1)
    #     temp = s[r]
    #     s[r] = s[l]
    #     s[l] = temp


    def reverseString(self, s):
        left = 0
        right = len(s)-1

        def helper(l, r):
            if l<=r:
                s[l], s[r] = s[r], s[l]
                helper(l+1, r-1)

        # self.recursion(s, left,right)
        helper(left,right)
        print(s)

Solution().reverseString(["h","e","l","l","o"])

