import sys

arr = [list(i) for i in sys.stdin.read().splitlines()]
n, m = len(arr), len(arr[0])
for i in range(n):
    for j in range(m):
        if arr[i][j] == "^":
            x, y = i, j
            break
vis = set()
dx, dy = -1, 0
while True:
    vis.add((x, y))
    if not (-1 < x + dx < n and -1 < y + dy < m):
        break
    elif arr[x + dx][y + dy] == "#":
        dx, dy = dy, -dx
    else:
        x += dx
        y += dy
print(len(vis))
