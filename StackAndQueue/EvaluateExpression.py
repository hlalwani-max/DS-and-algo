'''
https://www.interviewbit.com/problems/evaluate-expression/
Yahoo Google Facebook

Problem-

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Input Format
The only argument given is character array A.

Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.
For Example

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9

Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
'''


class Solution:
    _operations = ['*', '/', '+', '-']

    # @param A : list of strings
    # @return an integer
    # TC- O(N), SC- O(N), items pushed only once in array.
    # Idea - whenever an operand occurs pop elements a and b from stack, run operation and push it back in the stack.
    def evalRPN(self, A):
        stack = []

        for item in A:
            if item not in self._operations:
                stack.append(item)
            else:
                operand = item
                b = stack.pop()
                a = stack.pop()
                a, b = int(a), int(b)

                res = self.getresult(operand, a, b)
                stack.append(res)

        return stack[0]

    def getresult(self, op, x, y):
        if op == "*":
            return x * y
        elif op == "/":
            return x // y
        elif op == "+":
            return x + y
        else:
            return x - y


if __name__ == "__main__":
    exp_arr = ["4", "13", "5", "/", "+"]
    out = Solution().evalRPN(exp_arr)
    print("Solution of {} is: {}".format(exp_arr, out))
