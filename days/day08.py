"""
Day 08 Solver
"""
import math
import heapq
from collections import defaultdict


class Circuit:
    def __init__(self, index):
        self.members = {index}

    def merge(self, other):
        if other is self:
            return
        self.members |= other.members


class CircuitManager:
    def __init__(self, n):
        self.parent = list(range(n))
        self.circuits = [Circuit(i) for i in range(n)]

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if len(self.circuits[ra].members) < len(self.circuits[rb].members):
            ra, rb = rb, ra
        self.circuits[ra].merge(self.circuits[rb])
        self.parent[rb] = ra
        return True


def solve(data: str):
    lines = data.splitlines()
    points = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        x,y,z = map(int, parts)
        points.append((x,y,z))

    edges = []
    heap = []
    components = len(points)
    n = len(points)
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d2 = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
            edges.append((d2, i, j))
    edges.sort()

    K = len(points)
    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

            if len(heap) < K:
                heapq.heappush(heap, (-d, i, j))
            else:
                if d < -heap[0][0]:
                    heapq.heapreplace(heap, (-d, i, j))

    pairs = [(-d, i, j) for (d, i, j) in heap]
    pairs.sort()


    if K < 30:
        print("Edges: ", edges,"\n\n\nPairs: ", pairs)

    cm = CircuitManager(K)

    for dist, i, j in pairs:
        cm.union(i, j)

    sizes = defaultdict(int)
    for i in range(len(points)):
        sizes[cm.find(i)] += 1

    top3 = sorted(sizes.values(), reverse=True)[:3]
    part1 = top3[0] * top3[1] * top3[2]

    last_i = last_j = None
    for dist, i, j in edges:
        if cm.union(i, j):
            components -= 1
            last_i, last_j = i, j
            if components == 1:
                break
    x1, _, _ = points[last_i]
    x2, _, _ = points[last_j]
    part2 = x1 * x2

    return part1, part2

if __name__ == "__main__":
    print(solve("a\nb\nc"))
