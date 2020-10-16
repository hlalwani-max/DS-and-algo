'''
https://www.interviewbit.com/problems/permutations/
Microsoft Adobe Google
Concept - Backtracking (variation of combinations/subset problem)

Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    # TC- O(N*N!), SC- O(N!)
    # Idea- for generating each perm, add number and maintain which numbers are available to add to perm(using checker),
    # backtracking and find next combination.
    def permute(self, A):
        length = len(A)
        perm = []
        permutations = []
        checker = [0] * length
        self.generatePerm(A, checker, permutations, perm, length)
        return permutations

    def generatePerm(self, A, checker, permutations, perm, length):
        if len(perm) == length:
            permutations.append(list(perm))
        else:
            # start = 0 always, since for every new permutation, all elements are available
            for i in range(0, length):
                if checker[i] == 1:
                    continue
                # set checker to 1 when including- so it is unavailable for current combination.
                checker[i] = 1
                perm.append(A[i])
                self.generatePerm(A, checker, permutations, perm, length)
                # change checker back to 0- so it is available back again for new combination.
                checker[i] = 0
                perm.pop()

        return


if __name__ == "__main__":
    candidates = [1, 2, 3]
    out = Solution().permute(candidates)
    print("Possible permutations for {} are: {}".format(candidates, out))
