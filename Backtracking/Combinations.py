'''
https://www.interviewbit.com/problems/combinations/
Amazon Adobe
Concept- Backtracking (same as subsets problem)

Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    # TC- O(N * 2^N), SC - O(N * 2^N), two choices- to take that element or not.
    def combine(self, A, B):
        combo = []
        combinations = []
        start = 1
        self.generateCombo(A, B, combo, combinations, start)
        return combinations

    def generateCombo(self, n, k, combo, combinations, start):
        if len(combo) == k:
            combinations.append(list(combo))
            return

        for i in range(start, n + 1):
            combo.append(i)
            self.generateCombo(n, k, combo, combinations, i + 1)
            combo.pop()

    #  IB Solution.
    def combine1(self, A, B):
        A = list(range(1, A + 1))
        return self.generateCombo(A, B)

    def generateCombo1(self, A, B):
        if B <= 0:
            return []
        if B == 1:
            return [[item] for item in A]

        combinations = []
        for i in range(len(A)):
            # combo is list here, add two list.
            combinations += [[A[i]]+combo for combo in self.generateCombo(A[i+1:], B - 1)]

        return combinations


if __name__ == "__main__":
    n, k = 4, 3
    out = Solution().combine(n, k)
    print("combinations: \n", out)
