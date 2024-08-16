# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, profit = prices[0], 0
        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > profit:
                profit = p - min_price
        return profit
