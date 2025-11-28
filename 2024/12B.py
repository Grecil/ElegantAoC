import sys
from collections import deque
from itertools import count


def bfs(x, y):
    letter = grid[x][y]
    queue = deque([(x, y)])
    fences = set()
    vis[x][y] = True
    a = s = 0

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
                fences.add((r, c, dr, dc))
    while fences:
        r, c, dr, dc = fences.pop()
        s += 1
        for d in (1, -1):
            for i in count(d, d):
                f = (r + i * dc, c + i * dr, dr, dc)
                if f in fences:
                    fences.remove(f)
                else:
                    break
    return a, s


grid = [list(i) for i in sys.stdin.read().splitlines()]
n, m = len(grid), len(grid[0])
vis = [[False] * m for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            a, s = bfs(i, j)
            ans += a * s

print(ans)
