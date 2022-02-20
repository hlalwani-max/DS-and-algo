'''
https://www.interviewbit.com/problems/subsets-ii/
Amazon Microsoft
Concept- same as subsets problem.

Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    # TC - (N * 2^N), SC - (N * 2^N); every iteration go through two choice- in or out of stack.
    # Idea - iterate through array and find combination on two choices- in and out.
    def subsetsWithDup(self, A):
        A.sort()
        ind, length = 0, len(A)
        combinations = []
        curr_combo = []
        self.generateSubsets(A, combinations, curr_combo, ind, length)
        return combinations

    def generateSubsets(self, A, combinations, curr_combo, ind, length):
        # make new copy of perm to store in combinations, so changing original perm does not change them inside combinations.

        if curr_combo not in combinations:
            combinations.append(list(curr_combo))

        for i in range(ind, length):
            curr_combo.append(A[i])
            self.generateSubsets(A, combinations, curr_combo, i + 1, length)
            curr_combo.pop()



if __name__ == "__main__":
    arr = [1, 3, 2]
    out = Solution().subsetsWithDup(arr)
    print("Possible unique subsets (in ascending order) is: {}".format(out))
