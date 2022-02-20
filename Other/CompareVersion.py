# String- https://www.interviewbit.com/problems/compare-version-numbers/

'''
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.

Ex. 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
'''

from collections import deque


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # Using queue: TC- O(2*(N+M)), SC- O(N+M)
    def compareVersion1(self, A, B):
        q1 = deque(A.split("."))
        q2 = deque(B.split("."))

        l1, l2 = len(q1), len(q2)

        while q1 and q2:
            cur1 = q1.popleft()
            cur2 = q2.popleft()

            if int(cur1) > int(cur2):
                return 1
            elif int(cur1) < int(cur2):
                return -1

        if l1 > l2:
            while q1:
                cur1 = q1.popleft()
                if int(cur1) > 0:
                    return 1
        else:
            while q2:
                cur2 = q2.popleft()
                if int(cur2) > 0:
                    return -1

        return 0

    # without queue: TC- O(2*(N+M)), SC- O(N+M)
    def compareVersion(self, A, B):

        v1 = list(map(int, A.split(".")))
        v2 = list(map(int, B.split(".")))

        l1, l2 = len(v1), len(v2)
        diff = abs(l2 - l1)

        for i in range(diff):
            if l1 > l2:
                v2.append(0)
            elif l2 > l1:
                v1.append(0)

        # Append zeroes to handle variable strings
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        return 0


if __name__ == "__main__":
    str1, str2 = "1.21.1.1.1", "1.21.1.1.11"
    out = Solution().compareVersion(str1, str2)
    print(out)
