'''

Google Facebook Amazon
Concept-

Problem-
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
the ith histogram’s bar. Width of each bar is 1.

Largest Rectangle in Histogram: Example 1
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Largest Rectangle in Histogram: Example 2
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Find the area of largest rectangle in the histogram.

Input Format
The only argument given is the integer array A.

Output Format
Return the area of largest rectangle in the histogram.

For Example
Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
Explanation 1:
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Solution-

max_rectangle = 0
stack = an instance of empty stack
for index = 0 to all_histograms.length
    if stack.empty OR H[index] > H[stack.top]
        Push index to the stack
    if H[index] < H[stack.top]
        while !stack.empty && H[stack.top] > H[index]
            h = H[stack.pop]
            # Calculate the area with h as the smallest height.
            R = index
            L = stack.top
            max_rectangle = MAX(max_rectangle, (R - L - 1) * h)
        Push index to the stack
if stack is not empty
    Repeat the process of removing entries one by one from stack and calculating the max_rectangle as done earlier.

'''

import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        N = len(A)
        if M < 2:
            return A[N-1]
        maxx_area = 0

        stack = []
        for i in range(N):
            if stack and stack[-1] > A[i]:
                h = stack.pop()
                R = i
                if stack:
                    L = stack[-1]
                else:
                    L=0
                maxx_area = max(maxx_area, (R - L - 1) * h)

            if stack and stack[-1] < A[i]:
                R = i

            stack.append(A[i])

        return maxx_area

if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    out = Solution().largestRectangleArea(arr)
    print("Largest rectangle area for given heights is: {}".format(out))