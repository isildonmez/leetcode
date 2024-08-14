# https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
