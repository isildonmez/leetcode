from collections import deque

class Solution:
    def coords(self, grid: list[list[int]]) -> tuple[set[tuple[int]], set[tuple[int]]]:
        rows, columns = len(grid), len(grid[0])
        coords_0s = []
        coords_1s = []
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    coords_1s.append((i,j))
                elif grid[i][j] == 0:
                    coords_0s.append((i,j))
        return (coords_0s, coords_1s)

    def total_distances(self, coords: set[tuple[int]], grid: list[list[int]]) -> list[int]:
        all_distances = None
        rows, columns = len(grid), len(grid[0])
        id = 0
        for i,j in coords:
            current_distances = {}
            neighbours = deque()
            neighbours.append((i,j,id))
            while len(neighbours) > 0:
                x,y,d = neighbours.popleft()
                if x-1 >= 0 and grid[x-1][y] == 0 and (x-1,y) not in current_distances.keys():
                    neighbours.append((x-1,y,d+1))
                    current_distances[x-1,y] = d+1
                if x+1 < rows and grid[x+1][y] == 0 and (x+1, y) not in current_distances.keys():
                    neighbours.append((x+1,y,d+1))
                    current_distances[x+1,y] = d+1
                if y-1 >= 0 and grid[x][y-1] == 0 and (x, y-1) not in current_distances.keys():
                    neighbours.append((x,y-1,d+1))
                    current_distances[x,y-1] = d+1
                if y+1 < columns and grid[x][y+1] == 0 and (x, y+1) not in current_distances.keys():
                    neighbours.append((x,y+1,d+1))
                    current_distances[x,y+1] = d+1
            if all_distances is None:
                all_distances = current_distances
            else:
                intersection = all_distances.keys() & current_distances.keys()
                if len(intersection) == 0: return []
                common_distances = {}
                for c in intersection:
                    common_distances[c] = all_distances[c] + current_distances[c]
                all_distances = common_distances
        return list(all_distances.values())

    def shortestDistance(self, grid: list[list[int]]) -> int:
        if len(grid) == 0: return -1
        coords_0s, coords_1s = self.coords(grid)
        if len(coords_0s) == 0 or len(coords_1s) == 0:
            return -1
        total_distances = self.total_distances(coords_1s, grid)
        if len(total_distances) == 0: return -1
        min_distance = None
        for d in total_distances:
            if min_distance is None or min_distance > d:
                min_distance = d
        return min_distance


if __name__ == "__main__":
    s = Solution()
    print("Testing...")
    assert s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]) == 7
    assert s.shortestDistance([[1,0]]) == 1
    assert s.shortestDistance([[1]]) == -1
    assert s.shortestDistance([[1,1],[0,1]]) == -1
    assert s.shortestDistance([[0,2,0,2,2,0,2,2],[0,2,2,2,1,0,1,2],[0,0,0,1,0,2,0,0],[2,0,0,2,0,2,2,0],[0,0,0,2,0,0,0,0]]) == 11
    print("Done!")

