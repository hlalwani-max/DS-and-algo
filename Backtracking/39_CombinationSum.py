'''
https://www.interviewbit.com/problems/combination-sum/
https://leetcode.com/problems/combination-sum/

Facebook Amazon Adobe
Concept- same as subset problem.

Problem-
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.

Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:
[2, 2, 3]
[7]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    # TC- O(n^n(Math.pow(n,n))), since multiple occurance of same element.
    def combinationSum(self, A, B):
        A.sort()
        length = len(A)
        start = 0
        combo = []
        combinations = []

        self.findCombo(A, B, combinations, combo, start, length)
        return combinations

    def findCombo(self, A, B, combinations, combo, start, length):
        # check to make sure only unique combinations are added.
        if sum(combo) == B and combo not in combinations:
            combinations.append(list(combo))
            return

        #  if sum greater than target, return back
        if sum(combo) > B:
            return

        for i in range(start, length):
            combo.append(A[i])
            # include same element index i, to have elements included multiple times in combinations.
            self.findCombo(A, B, combinations, combo, i, length)
            combo.pop()

        return


if __name__ == "__main__":
    cand, target = [2, 3, 6, 7], 7
    out = Solution().combinationSum(cand, target)
    print("combinations: \n", out)
