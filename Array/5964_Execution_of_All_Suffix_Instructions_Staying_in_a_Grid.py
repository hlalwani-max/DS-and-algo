class Solution:
    def ifOffGrid(self, n, currPos, next):
        newPos = [currPos[0], currPos[1]]
        if next == 'L':
            newPos[1] = newPos[1] - 1
        elif next == 'R':
            newPos[1] = newPos[1] + 1
        elif next == 'U':
            newPos[0] = newPos[0] - 1
        else:
            newPos[0] = newPos[0] + 1

        if newPos[0] >= n or newPos[1] >= n or newPos[0] < 0 or newPos[1] < 0:
            return [True, currPos]
        else:
            return [False, newPos]

    def executeInstructions(self, n, startPos, s):
        ans = [0] * len(s)

        for i in range(len(ans)):
            curr_s = s[i:]
            count = 0
            currPos = [startPos[0], startPos[1]]
            for j in range(len(curr_s)):
                offGridRes = self.ifOffGrid(n, currPos, curr_s[j])
                if offGridRes[0]:
                    ans[i] = count
                    break
                else:
                    count += 1
                    currPos = offGridRes[1]
            ans[i] = count

        return ans


if __name__ == '__main__':
    # n, startPos, s = 3, [0,1], "RRDDLU"
    n, startPos, s = 1, [0,0], "LRUD"
    out = Solution().executeInstructions(n, startPos, s)
    print(out)
