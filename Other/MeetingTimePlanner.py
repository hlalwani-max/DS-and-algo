# Array
# https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5Lg1
def meeting_planner(slotsA, slotsB, dur):
    len_A = len(slotsA)  # 3
    len_B = len(slotsB)  # 2

    if (len_A == 0 or len_B == 0) or dur < 0:
        return []

    for i in range(len_A):
        x1, x2 = slotsA[i]

        for j in range(len_B):
            y1, y2 = slotsB[j]

            if x1 > y1:
                start = x1
                # desired_endtime = start + duration
                if y2 < x1:
                    # print("14",x1,x2,y1,y2)
                    continue

                if start + dur <= y2 and start + dur <= x2:
                    # print("18",x1,x2,y1,y2)
                    return [start, start + dur]
            else:
                start = y1

                if y1 > x2:
                    # print("23",x1,x2,y1,y2)
                    continue

                if start + dur <= x2 and start + dur <= y2:
                    # print("28",x1,x2,y1,y2)
                    return [start, start + dur]

    return []


slotA = [[1, 10]]
slotB = [[2, 3], [5, 7]]
durr = 2
print(meeting_planner(slotA, slotB, durr))

