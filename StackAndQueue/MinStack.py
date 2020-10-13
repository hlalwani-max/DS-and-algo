'''
https://www.interviewbit.com/problems/min-stack/
Yahoo Amazon Adobe Microsoft

Problem-
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.

'''

# TC- O(N), SC- O(N)
# Idea - maintain stack for minimum, if element is popped and is minimum, pop stack of minimums.
# While pushing, check if new minimum found, if so, append it on top of stack of minimums.
class MinStack:
    def __init__(self):
        self.stack = list()
        self.minstack = list()

    # @param x, an integer, return nothing
    def push(self, x):
        self.stack.append(x)
        if not self.minstack or (self.minstack and x < self.minstack[-1]):
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            popped_ele = self.stack.pop()

            if popped_ele == self.minstack[-1]:
                self.minstack.pop()

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if self.minstack:
            return self.minstack[-1]
        return -1


if __name__ == "__main__":
    s = MinStack()
    s.push(9)
    s.push(10)
    print("Min: ", s.getMin())
    s.pop()
    print("Min: ", s.getMin())
    s.pop()
    print("Min: ", s.getMin())
