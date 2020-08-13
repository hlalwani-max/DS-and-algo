# Array- Hotel booking possible
# https://www.interviewbit.com/problems/hotel-bookings-possible/


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean

    '''
    # for hotel1
        def sort(self, A, B, l):
            arr = []
            for i in range(l):
                arr.append((A[i], B[i]))

            arr = sorted(arr, key=lambda x: x[0])
            return arr
    '''

    def hotel(self, arrive, depart, K):
        # prioritize departure (0) for special cases cases
        times = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        times.sort()
        count = 0

        for time in times:
            # check if at anytime number of guests are more than available rooms
            if count > K:
                return 0
            # if guest arrives, count++
            if time[1] == 1:
                count += 1
                # if guest departs, count--
            else:
                count -= 1

        return 1

    # not working
    '''
        def hotel1(self, arrive, depart, K):
    
            l = len(arrive)
            arr_dep_sorted = self.sort(arrive, depart, l)
    
            count = 0
            # end = max(depart)
    
            for i in range(l):
                if i + 1 < l:
                    # given sorted arrive and depart check for overlap
                    if arr_dep_sorted[i][1] > arr_dep_sorted[i + 1][0]:
                        # remember number of overlaps as count
                        count += 1
    
                # check number of rooms minus one are greater than number of overlaps
                if count > K - 1:
                    return 0
            return 1
    '''


if __name__ == "__main__":
    sol = Solution()
    A = [1, 2, 3]
    B = [2, 3, 4]
    C = 1
    print("Input: ", A, B, C)
    ans = sol.hotel(A, B, C)
    print("Output: ", ans)
