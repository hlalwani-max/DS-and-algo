'''
Leetcode Contest-
Status- Wrong answer on example 4.

You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

You can apply either of the following two operations any number of times and in any order on s:

Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.



Example 1:

Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
Add:    "5121"
Rotate: "2151"
Add:    "2050"
There is no way to obtain a string that is lexicographically smaller then "2050".
Example 2:

Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
Add:    "42"
Rotate: "24"
There is no way to obtain a string that is lexicographically smaller then "24".
Example 3:

Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".
Example 4:

Input: s = "43987654", a = 7, b = 3
Output: "00553311"


Constraints:

2 <= s.length <= 100
s.length is even.
s consists of digits from 0 to 9 only.
1 <= a <= 9
1 <= b <= s.length - 1
'''


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        N = len(s)
        odd = False

        if N == 0:
            return s

        # if b is even, we can maniplate odd digits too by rotating first.
        if b & 1:
            odd = True

        if odd:
            # rotate s at least once so we can also manipulate odd digits. (zero based)
            s = self.addOddIndices(s, N, a)
            print(s)
            s = self.rotateOnce(s, N, b)
            s = self.addOddIndices(s, N, b)
            print(s)
        else:
            s = self.addOddIndices(s, N, a)

        # print(s)
        s = self.rotate(s, N, b)

        return s

    def rotateOnce(self, ss, length, b):
        if length == 1:
            return ss
        else:
            limit = b
            new_s = ss
            while limit > 0:
                new_s = new_s[-1] + new_s[:-1]
                limit -= 1

            return new_s

    def rotate(self, ss, length, b):
        if length == 1:
            return ss

        for i in range(length // b + 1):
            limit = b
            new_s = ss
            while limit > 0:
                new_s = new_s[-1] + new_s[:-1]
                limit -= 1

            if int(new_s) < int(ss):
                ss = new_s

        return ss

    def addOddIndices(self, ss, length, a):
        i = 1
        while i < length:
            while int(str(int(ss[i]) + a)[-1]) < int(ss[i]):
                ss = ss[:i] + str(int(ss[i]) + a)[-1] + ss[i + 1:]
            i += 2

        return ss


if __name__ == "__main__":
    s, a, b = "43987654", 7, 3
    # s, a, b = "74", 5, 1
    out = Solution().findLexSmallestString(s, a, b)
    print("smallest lexilogical string for input is: {}".format(out))
