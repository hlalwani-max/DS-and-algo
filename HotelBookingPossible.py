# Array- Hotel booking possible
# https://www.interviewbit.com/problems/hotel-bookings-possible/


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        l = len(arrive)
        count = 0

        for i in range(l):
            if i + 1 < l:
                # given sorted arrive and depart check for overlap
                if depart[i] > arrive[i + 1]:
                    # remember number of overlaps as count
                    count += 1

            # check number of rooms minus one are greater than number of overlaps
            if count > K-1:
                return 0
        return 1


if __name__ == "__main__":
    sol = Solution()
    A = [1, 3, 5, 7]
    B = [2, 6, 8, 10]
    C = 3
    print("Input: ", A, B, C)
    ans = sol.hotel(A, B, C)
    print("Output: ", ans)
