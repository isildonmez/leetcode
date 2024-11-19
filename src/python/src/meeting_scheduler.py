# https://leetcode.com/problems/meeting-scheduler/?envType=company&envId=datadog&favoriteSlug=datadog-thirty-days

from typing import Optional


class Solution:
    def minAvailableDuration(
        self, slots1: list[list[int]], slots2: list[list[int]], duration: int
    ) -> list[int]:
        i = j = 0
        slots1, slots2 = filter_durations(slots1, duration), filter_durations(
            slots2, duration
        )
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            if s2 > e1:
                i += 1
                continue
            if s1 > e2:
                j += 1
                continue
            start, end = max(s1, s2), min(e1, e2)
            if end - start >= duration:
                return [start, start + duration]
            if e1 > e2:
                j += 1
            elif e2 > e1:
                i += 1
            else:
                i += 1
                j += 1
        return []


def filter_durations(
    slots: list[list[int]], duration: int
) -> Optional[list[list[int]]]:
    return [slot for slot in slots if slot[1] - slot[0] >= duration]
