'''
https://www.interviewbit.com/problems/nearest-smaller-element/
Amazon Microsoft
Concept (same as MAXSPPROD problem)- using stack to replace all higher or equal values in stack for current value.

Problem-
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,
    G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Input Format
The only argument given is integer array A.

Output Format
Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element occurs G[i] should be -1.
For Example

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]

Input 2:
    A = [3, 2, 1]
Output 2:
    [-1, -1, -1]
Explaination 2:
    index 1: No element less than 3 in left of 3, G[1] = -1
    index 2: No element less than 2 in left of 2, G[2] = -1
    index 3: No element less than 1 in left of 1, G[3] = -1
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    # TC- O(n), SC- O(n), because array is only traversed once, and elements in stack only pushed  and popped once adding total complexity to O(3n).
    # Idea- for ith element, remove all the elements in stack that are greater than or equal to ith, and add ith element to stack.
    # Doing so, at each point you have lower value elements left from 0 to i-1 closest to i.
    def prevSmaller(self, A):
        N = len(A)
        ans = [-1]*N

        stack = []
        for i in range(N):
            # When processing the ith element remove all the elements from the stack which have value greater than or equal to ith element.
            while stack and A[i] <= stack[-1]:
                stack.pop()

            # Compare curr with stack top.
            if stack and stack[-1] < A[i]:
                ans[i] = stack[-1]

            # add curr to stack
            stack.append(A[i])

        return ans


if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    out = Solution().prevSmaller(arr)
    print("Previous smaller element for array {} is:\n{}".format(arr, out))
