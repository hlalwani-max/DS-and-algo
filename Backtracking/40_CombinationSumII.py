'''
https://www.interviewbit.com/problems/combination-sum-ii/
Microsoft Amazon Infosys
Concept- same as combinationSum (finding subsets)

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        start, length = 0, len(A)
        combo = []
        combinations = []

        self.generateCombo(A, B, combinations, combo, start, length)
        return combinations

    def generateCombo(self, A, B, combinations, combo, start, length):
        if sum(combo) == B and combo not in combinations:
            combinations.append(list(combo))
            return

        if sum(combo) > B:
            return

        for i in range(start, length):
            combo.append(A[i])
            self.generateCombo(A, B, combinations, combo, i + 1, length)
            combo.pop()

        return


if __name__ == "__main__":
    cand, target = [10, 1, 2, 7, 6, 1, 5], 8
    out = Solution().combinationSum(cand, target)
    print("combinations: \n", out)
