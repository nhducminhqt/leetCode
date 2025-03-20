from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weights = [131071] * n  # 2^17 - 1 (max 17-bit integer)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, w):
        repX = self.find(x)
        repY = self.find(y)
        if repX != repY:
            if self.rank[repX] >= self.rank[repY]:
                self.parent[repY] = repX
                self.rank[repX] += self.rank[repY]
            else:
                self.parent[repX] = repY
                self.rank[repY] += self.rank[repX]
        # Update min AND weight for the component
        self.weights[repX] = self.weights[repY] = self.weights[repX] & self.weights[repY] & w

    def path_weight(self, node):
        return self.weights[self.find(node)]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = UnionFind(n)

        # Build DSU with edges
        for u, v, w in edges:
            dsu.union(u, v, w)

        res = []
        for s, t in query:
            if dsu.find(s) == dsu.find(t):
                res.append(dsu.path_weight(s))
            else:
                res.append(-1)

        return res