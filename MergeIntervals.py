# Definition for an interval.
import sys


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if not intervals:
            return [new_interval]
        res = []
        lI = len(intervals)
        if new_interval.end < intervals[0].start:
            #     insert new interval in the beginning
            res.append(new_interval)
            res += intervals
            return res
        elif new_interval.start > intervals[lI - 1].end:
            intervals.append(new_interval)
            return intervals
        else:
            start, end = sys.maxint, -sys.maxint
            for ind, interval in enumerate(intervals):
                if interval.start <= new_interval.start <= interval.end:
                    start = ind

            for ind, interval in enumerate(intervals):
                if interval.start <= new_interval.end <= interval.end:
                    end = ind
            # consider cases where 1. no overlap found, 2. only start overlap found. 3. Only end overlap found
            if start != sys.maxin and end== -sys.maxint:
                start
                return [new_interval]

            for i in range(start):
                res.append(intervals[i])

            tmpInterval = Interval(min([intervals[start].start, new_interval.start]),
                                   max([intervals[end].end, new_interval.end]))
            res.append(tmpInterval)

            for i in range(end + 1, lI):
                res.append(intervals[i])

        #         find overalap start
        # pick lesser of interval.start and new_interval.start
        # traverse till you find overlap for interval.end, pick greater of interval.end and new_interval.end

        return res


inp = [Interval(5, 10), Interval(20, 30)]
merge = Interval(31, 40)

out = Solution().insert(inp, merge)
out = [(item.start, item.end) for item in out]
print(out)

'''
[(1,4) (6,8)]
insert (2,3)
insert (7,8)
insert (4,6)
insert extreme left
insert extreme right
'''
