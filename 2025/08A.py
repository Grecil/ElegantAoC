import sys
from math import prod


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


arr = [tuple(map(int, i.strip().split(","))) for i in sys.stdin.readlines()]
n = len(arr)
pairs = []
for i in range(n - 1):
    x, y, z = arr[i]
    for j in range(i + 1, n):
        a, b, c = arr[j]
        pairs.append(((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2, i, j))
pairs.sort(reverse=True)
dsu = DisjointSetUnion(n)
for _ in range(1000):
    d, i, j = pairs.pop()
    if dsu.find(i) == dsu.find(j):
        continue
    dsu.union(i, j)
st = {dsu.find(i) for i in range(n)}
sizes = sorted(dsu.size[i] for i in st)
print(prod(sizes[-3:]))
