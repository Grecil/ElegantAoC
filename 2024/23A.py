import sys
from collections import defaultdict

edges = [i.split("-") for i in sys.stdin.read().splitlines()]
triplets = set()
seen = defaultdict(set)
for x, y in edges:
    triplets |= set(tuple(sorted((x, y, i))) for i in seen[y] & seen[x])
    seen[x].add(y)
    seen[y].add(x)

print(sum(any(j[0] == "t" for j in i) for i in triplets))
