import sys


def search(x, y, dx, dy):
    vis = set()
    while True:
        if (x, y, dx, dy) in vis:
            return 1
        vis.add((x, y, dx, dy))
        if not (-1 < x + dx < n and -1 < y + dy < m):
            return 0
        elif arr[x + dx][y + dy] == "#":
            dx, dy = dy, -dx
            continue
        x, y = x + dx, y + dy


arr = [list(i) for i in sys.stdin.read().splitlines()]
n, m = len(arr), len(arr[0])
for i in range(n):
    for j in range(m):
        if arr[i][j] == "^":
            x, y = i, j
            break
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != "#":
            arr[i][j] = "#"
            ans += search(x, y, -1, 0)
            arr[i][j] = "."
print(ans)
