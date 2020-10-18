'''
https://www.interviewbit.com/problems/palindrome-partitioning/
Amazon Google

Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
'''


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        start, length = 0, len(A)
        combinations = []
        combo = []
        partition = 1
        return self.dfs(A)
        # return combinations

    def dfs(self, s):
        # return [[s[:i]] + rest for i in range(1, len(s) + 1) for rest in self.dfs(s[i:])] or [[]]
        for i in range(1, len(s) + 1):
            for rest in self.dfs(s[i:]) or [[]]:
                if s[:i] == s[i - 1::-1]:
                    return [[s[:i]] + rest]


if __name__ == "__main__":
    s = "aaa"
    out = Solution().partition(s)
    print("Palindrome partitioning for the given string {} is: \n {}".format(s, out))
