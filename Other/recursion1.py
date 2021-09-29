class Solution:
    arr = [10, 12, 15, 32, 21]
    ln = len(arr)
    str = "madam"
    a = 2
    b = 5

    def power(self):
        return self.powerHelper(self.a, self.b, 1)

    def powerHelper(self, x, y, num):
        if y <= 0:
            return num
        num = x * self.powerHelper(x, y - 1, num)
        return num

    def palindromeCheck(self):
        l = len(self.str)
        if l == 0:
            return True
        if l == 1:
            return False
        mid = int(l / 2) - 1
        bool = self.palindromeHelper(self.str, 0, l - 1, mid, True)
        if bool == False:
            return False
        return True

    def palindromeHelper(self, str, i, j, mid, status):
        if i > mid or j < mid:
            return status
        if status == False:
            return False
        if str[i] != str[j]:
            status = False
            return False
        return self.palindromeHelper(str, i + 1, j - 1, mid, status)

    def printArray(self):
        self.helper(self.arr, 0, self.ln)

    def helper(self, arr, i, l):
        if i >= l:
            return
        print(arr[i])
        self.helper(arr, i + 1, l)


if __name__ == "__main__":
    sol = Solution()

    print("Print array-")
    sol.printArray()

    print("Palindrome check result-")
    print(sol.palindromeCheck())

    print("Power result:")
    print(sol.power())
