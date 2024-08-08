# https://leetcode.com/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150


from collections import deque


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_of_paths = 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if n == 0:
            return 0
        locations = deque()
        locations.append((0, 0))
        while len(locations) > 0:
            i, j = locations.popleft()
            if (i == m - 1 and j == n - 2) or (i == m - 2 and j == n - 1):
                num_of_paths += 1
                continue
            if j + 1 < n and obstacleGrid[i][j + 1] == 0:
                locations.append((i, j + 1))
            if i + 1 < m and obstacleGrid[i + 1][j] == 0:
                locations.append((i + 1, j))
        return num_of_paths


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    print("Done!")
