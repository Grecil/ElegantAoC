import sys
from collections import defaultdict

arr = sys.stdin.read().splitlines()
d = defaultdict(list)
n, m = len(arr), len(arr[0])
for i in range(n):
    for j in range(m):
        if arr[i][j] != ".":
            d[arr[i][j]].append((i, j))
an = set()
for i in d:
    temp = d[i]
    x = len(temp)
    an.update(temp)
    for j in range(x - 1):
        for k in range(j + 1, x):
            diff = (temp[j][0] - temp[k][0], temp[j][1] - temp[k][1])
            p1 = (temp[j][0] + diff[0], temp[j][1] + diff[1])
            while -1 < p1[0] < n and -1 < p1[1] < m:
                an.add(p1)
                p1 = (p1[0] + diff[0], p1[1] + diff[1])
            p2 = (temp[k][0] - diff[0], temp[k][1] - diff[1])
            while -1 < p2[0] < n and -1 < p2[1] < m:
                an.add(p2)
                p2 = (p2[0] - diff[0], p2[1] - diff[1])
print(len(an))
