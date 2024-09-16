# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0]
        for idx in range(1, len(intervals)):
            c_start, c_end = intervals[idx]
            if end >= c_start:
                end = max(end, c_end)
            else:
                result.append([start, end])
                start, end = c_start, c_end
        result.append([start, end])
        return result
