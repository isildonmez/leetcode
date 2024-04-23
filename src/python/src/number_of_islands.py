def exhaust_island(grid: list[list[str]], i: int, j: int) -> list[list[str]]:
    m = len(grid)
    n = len(grid[0])
    grid[i][j] = "-"
    if i - 1 >= 0 and grid[i - 1][j] == "1":
        exhaust_island(grid, i - 1, j)
    if i + 1 < m and grid[i + 1][j] == "1":
        exhaust_island(grid, i + 1, j)
    if j - 1 >= 0 and grid[i][j - 1] == "1":
        exhaust_island(grid, i, j - 1)
    if j + 1 < n and grid[i][j + 1] == "1":
        exhaust_island(grid, i, j + 1)
    return grid


class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        if grid == [] or grid[0] == []:
            return 0
        m, i = len(grid), 0
        n, j = len(grid[0]), 0
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid = exhaust_island(grid, i, j)
                    islands += 1
        return islands


if __name__ == "__main__":
    grid_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    grid_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    s = Solution()
    print("Testing...")
    assert s.num_islands(grid_1) == 1
    assert s.num_islands(grid_2) == 3
    print("Done!")
