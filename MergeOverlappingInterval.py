# Array- https://www.interviewbit.com/problems/merge-overlapping-intervals/
# Time complexity- O(nlogn + n), Space complexity- O(n)
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge1(self, intervals):
        res = []
        lI = len(intervals)
        start = 0

        # sort intervals on start time
        intervals = sorted(intervals, key=lambda x: x.start)
        # print("sorted interval:", [(item.start, item.end) for item in intervals])

        # O(n) traversal of intervals array
        while start < lI - 1:
            tmp = start + 1
            count = 0
            overlap = [intervals[start].start, intervals[start].end]

            # start looking for overlaps and club them, count= number of overlaps
            while tmp < lI:
                if overlap[1] >= intervals[tmp].start:
                    overlap[0] = min([overlap[0], intervals[tmp].start])
                    overlap[1] = max([overlap[1], intervals[tmp].end])
                    count += 1
                else:
                    break
                tmp += 1

            # if overlap found, push updated window
            if count > 0:
                newInterval = Interval(overlap[0], overlap[1])
                res.append(newInterval)
                # bring start pointer to next element
                start = start + count
            else:
                res.append(intervals[start])

            start += 1

        if start == lI - 1:
            res.append(intervals[start])

        return res

#     interviewbit solution
    def merge(self, intervals):
        res = []
        lI = len(intervals)
        intervals.sort(key=lambda x: x.start)

        for i,interval in enumerate(intervals):
            if res and interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)

        return res


inp = [Interval(1, 1), Interval(4, 5), Interval(2, 4), Interval(7, 10)]
out = Solution().merge(inp)
print([(item.start, item.end) for item in out])
