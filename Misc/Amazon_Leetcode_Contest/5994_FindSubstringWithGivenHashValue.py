class Solution:
    def subStrHash(self, s, power, modulo, k, hashValue):
        length = len(s)
        for i in range(length):
            temp = ""
            if len(temp) >= k:
                continue
            for j in range(i, length):
                temp += s[j]
                if len(temp) == k and self.getHashValue(temp, power, modulo, k) == hashValue:
                    return temp

    def getHashValue(self, s, p, m, k):
        dict = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26,
        }

        sum = 0

        for i in range(k):
            sum += (dict[s[i]] * (p ** i))

        return sum % m


s, p, m, k, h = "xxterzixjqrghqyeketqeynekvqhc", 15, 94, 4, 16
ans = Solution().subStrHash(s, p, m, k, h)
print(ans)
