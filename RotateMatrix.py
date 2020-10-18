# Interviewbit - haven't done efficient solution using graph and no additional space
import copy


class Solution:
    # with copy array
    # @param A : list of list of integers
    # @return the same list modified
    def rotate1(self, A):
        n = len(A)
        if n == 0:
            return []

        A_copy = copy.deepcopy(A)

        x = n - 1
        y = 0

        # decrease x in j , reset x in i and increase y in i

        for i in range(n):
            for j in range(n):
                # print(x, y)

                A[i][j] = A_copy[x][y]
                x -= 1

            x = n - 1
            y += 1

        return A

    # without copy array
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        if n == 0:
            return []

        dict = {}

        x = n - 1
        y = 0

    # decrease x in j , reset x in i and increase y in i

        for i in range(n):
            for j in range(n):
                # print(x, y)

                A[i][j] = A_copy[x][y]
                x -= 1

            x = n - 1
            y += 1



        return A


ans = Solution().rotate([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

for item in ans:
    print(item)

'''
input =
[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

ans =
[
    [13,9,5,1],
    [14,10,6,2],
    [15,11,7,3],
    [16,12,8,4]
]

indexes:

original-

[
    [(0,0),(0,1),(0,2),(0,3)],
    [(1,0),(1,1),(1,2),(1,3)],
    [(2,0),(2,1),(2,2),(2,3)],
    [(3,0),(3,1),(3,2),(3,3)]
]

[
    [(3,0),(2,0),(1,0),(0,0)],
    [(3,1),(2,1),(1,1),(0,1)],
    [(3,2),(2,2),(1,2),(0,2)],
    [(3,3),(2,3),(1,3),(0,3)]
]

0,0 -> 3,0
3,0 -> 3,3

0,1 -> 2,0
2,0 -> 3,2

0,2 -> 1,0
1,0 -> 3,1

0,3 -> 0,0
0,0 -> 3,0 (repeat)

1,0 -> 3,1
3,1 -> 2,3
'''
