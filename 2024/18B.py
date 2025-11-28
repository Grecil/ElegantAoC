import sys
from collections import deque
from bisect import bisect_left

arr = [list(map(int, i.split(","))) for i in sys.stdin.read().splitlines()]


def search(ind):
    grid = [[1] * 71 for _ in range(71)]
    for i, j in arr[:ind]:
        grid[i][j] = 0
    q = deque([(0, 0, 0)])
    vis = [[False] * 71 for _ in range(71)]
    while q:
        x, y, dist = q.popleft()
        vis[x][y] = True
        if (x, y) == (70, 70):
            return False
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if -1 < nx < 71 and -1 < ny < 71 and grid[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx, ny, dist + 1))
    return True


print(*arr[bisect_left(range(1024, len(arr) + 1), True, key=search) + 1023], sep=",")
