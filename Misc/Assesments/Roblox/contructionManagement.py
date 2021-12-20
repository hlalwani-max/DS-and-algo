
class Solution:
    def minCost(cost):
        number_of_houses = len(cost)
        dp = []
        # print(number_of_houses)
        # print(cost)
        for _ in range(number_of_houses):
            dp.append(([0] * 3))

        # print(dp)
        # for i in range(number_of_houses):
        #    dp[0][i] = cost[0][i]
        dp[0][0] = cost[0][0]
        dp[0][1] = cost[0][1]
        dp[0][2] = cost[0][2]
        # print(dp)
        for i in range(1, number_of_houses):
            for material in range(3):
                temp = [val for index, val in enumerate(dp[i - 1]) if index != material]
                # print(i, material, temp)
                dp[i][material] = cost[i][material] + min(temp)

        # print('\n')
        # print(dp)
        return min(dp[-1][0], dp[-1][1], dp[-1][2])
