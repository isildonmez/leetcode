# from https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75

from collections import deque


class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        for idx, r in enumerate(self.requests):
            if r >= t - 3000:
                self.requests = self.requests[idx:]
                break
        return len(self.requests)


class AlternativeRecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
