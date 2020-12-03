'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
'''
import sys


class Solution:
    def minimumEffortPath(self, heights) -> int:
        seen = set()
        x, y = 0, 0
        px, py = 0, 0
        seen.add((x, y))
        bx, by = len(heights) - 1, len(heights[0]) - 1
        gx, gy = bx, by
        effort = 0

        while (x, y) != (gx, gy):
            # check
            minEffort = sys.maxsize
            # minX, minY = x+1, y
            for x, y in (x+1, y), (x, y+1), (x-1, y), (y-1, x):
                if (x, y) == (gx, gy):
                    effort += abs(heights[x][y] - heights[px][py])
                    return minEffort
                if x > gx or y > gy or x < 0 or y < 0:
                    continue
                if (x,y) in seen:
                    continue
                # if abs(heights[x][y] - heights[px][py]) == 0:
                #     break
                else:
                    effort = abs(heights[x][y] - heights[px][py])
                    if effort < minEffort:
                        minX = x
                        minY = y
                        minEffort = effort

            if minX and minY:
                x, y = minX, minY
                effort += minEffort
                seen.add((x,y))

        return effort




if __name__ == '__main__':
    H = [[1,2,2],[3,8,2],[5,3,5]]
    out = Solution().minimumEffortPath(H)
    print("Minimum Effort to reach is: {}".format(out))