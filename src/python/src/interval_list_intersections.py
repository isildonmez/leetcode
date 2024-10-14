# https://leetcode.com/problems/interval-list-intersections/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            start_i, end_i = firstList[i]
            start_j, end_j = secondList[j]
            start = max(start_i, start_j)
            end = min(end_i, end_j)
            if start <= end:
                res.append([start, end])
            if end_i > end_j:
                j += 1
            elif end_i < end_j:
                i += 1
            else:
                i += 1
                j += 1
        return res


# firstList  = [[0,2],[5,10],[13,23],[24,25]],
# secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output:      [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
