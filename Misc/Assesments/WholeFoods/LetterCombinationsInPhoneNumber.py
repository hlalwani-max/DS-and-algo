'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Problem-

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''


class Solution:
    _mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    # TC = O(3^N * 4^N), N = number of elements in input that has 3 mappings, M = number of elements that has 4 mappings.
    # Idea- Use DFS to explore [:length of digits], when ind == length, append to combination.
    def letterCombinations(self, digits):
        N = len(digits)
        combinations = []

        if N == 0:
            return combinations
        else:
            self.helper(0, N, "", digits, combinations)
            return combinations

    def helper(self, ind, length, combo, digits, combinations):
        if ind == length:
            combinations.append(combo)
            return

        for letter in self._mapping[digits[ind]]:
            newCombo = combo + letter
            self.helper(ind + 1, length, newCombo, digits, combinations)

    # TC = O(3^N * 4^N), N = number of elements in input that has 3 mappings, M = number of elements that has 4 mappings.
    # SC - O(3^N * 4^N)
    # Idea (Naive) - Run combinations of two at a time and repeat.
    def letterCombinations1(self, digits):
        N = len(digits)
        combinations = []

        if N == 0:
            return []

        for alpha in self._mapping[digits[0]]:
            combinations.append(alpha)

        if N == 1:
            return combinations

        return self.helper(1, N, digits, combinations)

    def helper(self, ind, length, digits, combinations):
        if ind >= length:
            return combinations

        tmp = []
        for combination in combinations:
            for alpha in self._mapping[digits[ind]]:
                tmp.append(combination + alpha)

        combinations = tmp

        return self.helper(ind + 1, length, digits, combinations)


if __name__ == "__main__":
    str = "23"
    out = Solution().letterCombinations(str)
    print("Possible letter combinations is:", out)
