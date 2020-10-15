'''
https://www.interviewbit.com/problems/subset/
amazon microsoft
Concept- Backtracking and choices.

Problem-

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
'''

'''
class Solution:
# @param A : list of integers
# @return a list of list of integers
    def subsets(self, A):
        subset=[]
        index = 0
        A.sort()
        self.subsetsUtil(A, subset,[], index)
        return subset

    def subsetsUtil(self,A, subset,curr,index):
        subset.append(list(curr))
        for i in range(index, len(A)):
            curr.append(A[i])
            self.subsetsUtil(A, subset,curr, i + 1)
            curr.pop()
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    # TC - (N * 2^N), SC - (N * 2^N); every iteration go through two choice- in or out of stack.
    # Idea - iterate through array and find combination on two choices- in and out.
    def subsets(self, A):
        A.sort()
        ind, length = 0, len(A)
        combinations = []
        curr_combo = []
        self.generateSubsets(A, combinations, curr_combo, ind, length)
        return combinations

    def generateSubsets(self, A, combinations, curr_combo, ind, length):
        # make new copy of perm to store in combinations, so changing original perm does not change them inside combinations.
        combinations.append(list(curr_combo))

        for i in range(ind, length):
            curr_combo.append(A[i])
            self.generateSubsets(A, combinations, curr_combo, i + 1, length)
            curr_combo.pop()

    # TC - (N * 2 ^ N), SC - (N * 2 ^ N)
    # Idea - Using cascading: Let's start from empty subset in output list. At each step one takes new integer into
    # consideration and generates new subsets from the existing ones.
    def subsets1(self, nums):
        nums.sort()
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


if __name__ == "__main__":
    arr = [1, 3, 2]
    out = Solution().subsets1(arr)
    print("Possible unique subsets (in ascending order) is: {}".format(out))
