class Solution:
    def exhaust_island(self, grid: list[list[int]], i: int, j: int, id: int) -> int:
        size = 1
        grid[i][j] = id
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            size += self.exhaust_island(grid, i - 1, j, id)
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            size += self.exhaust_island(grid, i + 1, j, id)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            size += self.exhaust_island(grid, i, j - 1, id)
        if j + 1 < len(grid) and grid[i][j + 1] == 1:
            size += self.exhaust_island(grid, i, j + 1, id)
        return size

    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        id = 2
        sizes = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                size = self.exhaust_island(grid, i, j, id)
                sizes[id] = size
                id += 1
        largest_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                neighbours = set()
                if i - 1 >= 0 and grid[i - 1][j] != 0:
                    neighbours.add(grid[i - 1][j])
                if i + 1 < len(grid) and grid[i + 1][j] != 0:
                    neighbours.add(grid[i + 1][j])
                if j - 1 >= 0 and grid[i][j - 1] != 0:
                    neighbours.add(grid[i][j - 1])
                if j + 1 < len(grid) and grid[i][j + 1] != 0:
                    neighbours.add(grid[i][j + 1])
                total_size = sum(sizes[n] for n in neighbours) + 1
                largest_island = max(largest_island, total_size)
        return largest_island if largest_island != 0 else n**2


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.largestIsland([[1, 0], [0, 1]]) == 3
    assert s.largestIsland([[1, 1], [1, 0]]) == 4
    assert s.largestIsland([[1, 1], [1, 1]]) == 4
    print("Done!")
