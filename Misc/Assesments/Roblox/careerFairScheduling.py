# 'https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/'
# Solution- https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/discuss/933302/Python-Priority-Queue-in-O(k%2Bnlogn)

import heapq

def generateEvents(arrival, duration):
    events = []
    for i in range(len(arrival)):
        start, end = arrival[i], arrival[i] + duration[i]
        events.append([start, end])

    return events

def findMaxEvents(events):
    events.sort()
    res, d = 0, events[0][0]
    heap = []
    while events or heap:
        # Add new events that can be attended on day `d`
        while len(events) > 0 and events[0][0] == d:
            heapq.heappush(heap, events.pop(0)[1])

            # remove events that are already completed
        while heap and heap[0] < d:
            heapq.heappop(heap)

        # attend one event in day `d`
        if len(heap) > 0:
            res += 1
            heapq.heappop(heap)

        d += 1
    return res

def maxEvents(arrival, duration):
    events = generateEvents(arrival, duration)
    return(findMaxEvents(events))


if __name__ == '__main__':
    arrival, duration = [1, 3, 5], [2, 2, 2]
    print(maxEvents(arrival, duration))