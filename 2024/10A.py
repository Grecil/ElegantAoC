import sys


def bfs(x, y):
    ans, q = set(), [(x, y)]
    while q:
        x, y = q.pop(0)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if -1 < x + dx < n and -1 < y + dy < m and arr[x + dx][y + dy] == arr[x][y] + 1:
                if arr[x + dx][y + dy] == 9:
                    ans.add((x + dx, y + dy))
                else:
                    q.append((x + dx, y + dy))
    return len(ans)


arr = [[int(i) for i in list(j)] for j in sys.stdin.read().splitlines()]
n, m = len(arr), len(arr[0])
print(sum(bfs(i, j) if arr[i][j] == 0 else 0 for i in range(n) for j in range(m)))
