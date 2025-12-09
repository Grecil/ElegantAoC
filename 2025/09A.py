import sys
from collections import defaultdict

rects = [tuple(map(int, i.split(","))) for i in sys.stdin.readlines()]
d = defaultdict(lambda: [float("inf"), 0])
for x, y in rects:
    d[x][0] = min(d[x][0], y)
    d[x][1] = max(d[x][1], y)
ans = 0
for x1 in d:
    for x2 in d:
        r1 = (abs(x1 - x2) + 1) * (abs(d[x1][0] - d[x2][1]) + 1)
        r2 = (abs(x1 - x2) + 1) * (abs(d[x1][1] - d[x2][0]) + 1)
        ans = max(ans, r1, r2)
print(ans)
