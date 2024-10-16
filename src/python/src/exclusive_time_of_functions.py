# https://leetcode.com/problems/exclusive-time-of-functions/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


from collections import deque


class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        process_stack = deque()
        prev_time = 0
        for log in logs:
            pid, event, timestamp = log.split(":")
            pid, timestamp = int(pid), int(timestamp)
            if event == "start":
                if len(process_stack) > 0:
                    res[process_stack[-1]] += timestamp - prev_time
                process_stack.append(pid)
                prev_time = timestamp
            else:
                process_stack.pop()
                res[pid] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        return res
