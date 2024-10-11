from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        heads = deque()
        # (step_count, x, y)
        heads.append((1, 0, 0))
        grid[0][0] = 1
        n = len(grid)
        while len(heads) != 0:
            step_count, x, y = heads.popleft()
            if x == n - 1 and y == n - 1:
                return step_count
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i < 0 or i > n - 1:
                        continue
                    if j < 0 or j > n - 1:
                        continue
                    if grid[i][j] != 0:
                        continue
                    heads.append((step_count + 1, i, j))
                    grid[i][j] = 1
        return -1


if __name__ == "__main__":
    s = Solution()
    m = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]
    print("Testing...")
    assert s.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    assert s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert s.shortestPathBinaryMatrix(m) == 7
    print("Done!")
