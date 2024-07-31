# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        i = 0
        s0, e0 = intervals[i]
        while i < len(intervals) - 1:
            s1, e1 = intervals[i + 1]
            if e0 >= s1:
                e0 = max(e0, e1)
            else:
                result.append([s0, e0])
                s0, e0 = s1, e1
            i += 1
        result.append([s0, e0])
        return result
