'''
https://www.interviewbit.com/problems/maxspprod/

Concept- using stack to replace all lower or equal values in stack for current value.

Problem-
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (i>j). If multiple A[j]'s are present in multiple positions, the LeftSpecialValue is the maximum value of j.
RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (j>i). If multiple A[j]'s are present in multiple positions, the RightSpecialValue is the minimum value of j.
Write a program to find the maximum special product of any integer in the array.

NOTE: As the answer can be large, output your answer modulo 10^9 + 7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First and only argument is an integer array A.

Output Format
Return an integer denoting the maximum special product of any integer.

Example Input

Input 1:
 A = [1, 4, 3, 4]

Input 2:
 A = [10, 7, 100]

Example Output

Output 1:
 3
Output 2:
 0

Example Explanation

Explanation 1:
 For A[2] = 3, LeftSpecialValue is 1 and RightSpecialValue is 3.
 So, the ans is 1*3 = 3.

Explanation 2:
 There is not any integer having maximum special product > 0. So, the ans is 0.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    # TC- O(n), SC- O(n), because array is only traversed once, and elements in stack only pushed  and popped once adding total complexity to O(3n).
    # Idea- for ith element, remove all the elements in stack that are less than or equal to ith, and add ith element to stack.
    # Doing so, at each point you have greater value left from 0 to i-1 closest to i. Repeat same for rightValue in reverse order.
    def maxSpecialProduct(self, A):
        N = len(A)
        leftVal, rightVal = [0] * N, [0] * N

        # get left special array.
        stack = []
        for i in range(N):
            # When processing the ith element remove all the elements from the stack which have value less than or equal to ith element.
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()

            # compare stack top and current.
            if stack and A[stack[-1]] > A[i]:
                leftVal[i] = stack[-1]

            # Add curr element to the stack.
            stack.append(i)

        # repeat above for right, but in reverse order.
        stack.clear()
        for i in range(N - 1, -1, -1):
            # When processing the ith element remove all the elements from the stack which have value less than or equal to ith element.
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()

            # Since all lesser than A[i] elements are removed from stack, only greater are left. If not, default rightValue remains 0.
            if stack and A[stack[-1]] > A[i]:
                rightVal[i] = stack[-1]

            # Add curr element to the stack.
            stack.append(i)

        del(stack)

        # find max leftVal * rightVal
        max = -1
        for i in range(N):
            if leftVal[i] * rightVal[i] > max:
                max = leftVal[i] * rightVal[i]

        return max % 1000000007


if __name__ == "__main__":
    arr = [6, 7, 9, 5, 5, 8]
    out = Solution().maxSpecialProduct(arr)
    print("Max special product for the input is: {}".format(out))
