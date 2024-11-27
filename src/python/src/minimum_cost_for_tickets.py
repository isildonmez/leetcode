# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        costs_on_days = [0] * (days[-1] + 1)
        i = 0
        for day in range(1, days[-1] + 1):
            if day < days[i]:
                costs_on_days[day] = costs_on_days[day - 1]
                continue
            costs_on_days[day] = min(
                costs_on_days[day - 1] + costs[0],
                costs_on_days[max(0, day - 7)] + costs[1],
                costs_on_days[max(0, day - 30)] + costs[2],
            )
            i += 1
        return costs_on_days[-1]
