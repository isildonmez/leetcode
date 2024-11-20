def find_max_knapsack_profit(
    capacity: int, weights: list[int], values: list[int]
) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        for cap in range(capacity, weights[i] - 1, -1):
            dp[cap] = max(dp[cap], values[i] + dp[cap - weights[i]])
    return dp[capacity]
