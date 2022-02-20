'''
https://www.interviewbit.com/problems/maximal-string/
Apple
Problem Description

Given a string A and integer B, what is maximal lexicographical stringthat can be made from A if you do atmost B swaps.



Problem Constraints
1 <= |A| <= 9

A contains only digits from 0 to 9.

1 <= B <= 5



Input Format
First argument is string A.

Second argument is integer B.



Output Format
Return a string, the naswer to the problem.



Example Input
Input 1:

A = "254"
B = 1
Input 2:

A = "254'
B = 2


Example Output
Output 1:

 524
Output 2:

 542


Example Explanation
Explanation 1:

 Swap 2 and 5.
Explanation 2:

Swap 2 and 5 then swap 4 and 2.
'''


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        num = A
        ans = A
        i, j = 0, 1
        self.findGreaterNum(nums, ans, B, i, j)
        return ans

    def findGreaterNum(self, nums, ans, B, i, j):
        if B == 0:
            return

        if i<j and i < len(ans) and j < len(ans):
            ans[i], ans[j] = ans[j], ans[i]
            if int(ans) > int(nums):
                nums = ans
            self.findGreaterNum(self, nums, ans, B, i+1, j+1)


        return

if __name__ == "__main__":
    nums, swaps = "254", 2
    org_nums = nums
    out = Solution().solve(nums, swaps)
    print("Swapped number for {} with atmost {} swaps: {}".format(org_nums, swaps, out))