class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = []
        self.rank = [1] * (n + 1)
        for i in range(n+1):
            self.parent.append(i)
    
    def find_parent(self, v: int) -> int:
        if self.parent[v] != v:
            self.parent[v] = self.find_parent(self.parent[v])
        return self.parent[v]

    def union(self, v1: int, v2: int) -> bool:
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


def redundant_connections(edges: list[list[int]]) -> list[int]:
    uf = UnionFind(len(edges))
    for v1, v2 in edges:
        if not uf.union(v1, v2):
            return [v1, v2]