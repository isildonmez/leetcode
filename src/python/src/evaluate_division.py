# https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150


from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.values_to_values = defaultdict(lambda: {})

    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        for idx, [p1, p2] in enumerate((equations)):
            self.values_to_values[p1][p2] = values[idx]
            self.values_to_values[p2][p1] = 1 / values[idx]
        result = []
        for p1, p2 in queries:
            res = self.check_complement(p1, p2, 1, set())
            result.append(res)
        return result

    def check_complement(
        self, p1: int, p2: int, multiplier: float, visited: set[str]
    ) -> int:
        if p1 not in self.values_to_values or p2 not in self.values_to_values:
            return -1.0
        if p1 == p2:
            return multiplier
        if p2 in self.values_to_values[p1]:
            return self.values_to_values[p1][p2] * multiplier
        visited.add(p1)
        neighbours = self.values_to_values[p1]
        res = -1.0
        for neighbour, new_multiplier in neighbours.items():
            if neighbour in visited:
                continue
            new_multiplier *= multiplier
            temp_res = self.check_complement(
                neighbour, p2, new_multiplier, visited.copy()
            )
            if temp_res != -1.0:
                res = temp_res
                break
        return res
