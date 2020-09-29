'''
Two pointer- https://www.interviewbit.com/problems/3-sum-zero/ [Facebook, Google]

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        N = A.__len__()
        if N < 3: return []
        ans = set()

        for i in range(N - 1):
            j, k = i + 1, N - 1

            while j < k:
                pair = (A[i], A[j], A[k])
                cur_sum = A[i] + A[j] + A[k]

                if cur_sum == 0:
                    ans.add(pair)
                    j += 1
                elif cur_sum < 0:
                    j += 1
                else:
                    k -= 1

        return list(ans)


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    out = Solution().threeSum(arr)
    print("Result Triples- {}".format(out))
