import sys

rects = [tuple(map(int, i.split(",")))[::-1] for i in sys.stdin.readlines()]
n = len(rects)

# Coordinate Compression
xst, yst = set(), set()
for x, y in rects:
    xst.add(x)
    yst.add(y)
x2i = {x: i + 1 for i, x in enumerate(sorted(xst))}
y2i = {y: i + 1 for i, y in enumerate(sorted(yst))}

# Creating the boundary
lx, ly = len(x2i) + 2, len(y2i) + 2
grid = [[-1] * ly for i in range(lx)]
for i in range(len(rects)):
    x1, y1 = x2i[rects[i - 1][0]], y2i[rects[i - 1][1]]
    x2, y2 = x2i[rects[i][0]], y2i[rects[i][1]]
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            grid[x1][j] = 1
    else:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            grid[j][y1] = 1

# Making everything outside the boundary 0
stk = [(0, 0)]
while stk:
    x, y = stk.pop()
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if -1 < nx < lx and -1 < ny < ly and grid[nx][ny] == -1:
            grid[nx][ny] = 0
            stk.append((nx, ny))

# Making everything inside the boundary 1
for i in range(lx):
    for j in range(ly):
        if grid[i][j] == -1:
            grid[i][j] = 1

# 2D prefix sum to check if a rectangle is completely filled
pre = [[0] * (ly + 1) for _ in range(lx + 1)]
for i, row in enumerate(grid):
    pi, pii = pre[i], pre[i + 1]
    for j in range(ly):
        pre[i + 1][j + 1] = row[j] + pre[i][j + 1] + pre[i + 1][j] - pre[i][j]
csum = lambda a, b, x, y: pre[x][y] - pre[x][b] - pre[a][y] + pre[a][b]

# Make rectangles, check if they are filled and find the max area
ans = 0
for i in range(n - 1):
    x1, y1 = rects[i]
    for j in range(i + 1, n):
        x2, y2 = rects[j]
        a, b, c, d = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        ai, bi, ci, di = x2i[a], y2i[b], x2i[c], y2i[d]
        if csum(ai, bi, ci + 1, di + 1) == (ci - ai + 1) * (di - bi + 1):
            ans = max(ans, (c - a + 1) * (d - b + 1))
print(ans)
