# https://leetcode.com/problems/count-and-say/description/?envType=problem-list-v2&envId=a6ezkna5


class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        for _ in range(n - 1):
            current = self.count_and_say_current(current)
        return current

    def count_and_say_current(self, n: str) -> str:
        res = ""
        count = 1
        for i in range(1, len(n)):
            if n[i] == n[i - 1]:
                count += 1
                continue
            res += f"{count}{n[i-1]}"
            count = 1
        res += f"{count}{n[-1]}"
        return res
