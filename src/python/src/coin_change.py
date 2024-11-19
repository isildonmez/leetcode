# https://leetcode.com/problems/coin-change/description/?envType=company&envId=datadog&favoriteSlug=datadog-all


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
