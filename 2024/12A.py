import sys
from collections import deque


def bfs(x, y):
    letter = grid[x][y]
    queue = deque([(x, y)])
    vis[x][y] = True
    a = p = 0

    while queue:
        r, c = queue.popleft()
        a += 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == letter:
                if not vis[nr][nc]:
                    vis[nr][nc] = True
                    queue.append((nr, nc))
            else:
                p += 1

    return a, p


grid = [list(i) for i in sys.stdin.read().splitlines()]
n, m = len(grid), len(grid[0])
vis = [[False] * m for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            a, p = bfs(i, j)
            ans += a * p

print(ans)
