import sys

arr, moves = sys.stdin.read().split("\n\n")
moves = moves.replace("\n", "")
grid = [list(i) for i in arr.splitlines()]
n, m = len(grid), len(grid[0])
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if grid[i][j] == "@":
            x, y = i, j
            break
d = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
for move in moves:
    dx, dy = d[move]
    nx, ny = x + dx, y + dy
    while grid[nx][ny] != "#":
        if grid[nx][ny] == ".":
            while nx != x or ny != y:
                grid[nx][ny], grid[nx - dx][ny - dy] = grid[nx - dx][ny - dy], grid[nx][ny]
                nx, ny = nx - dx, ny - dy
            x, y = x + dx, y + dy
            break
        nx, ny = nx + dx, ny + dy
print(sum(100 * i + j if grid[i][j] == "O" else 0 for i in range(1, n - 1) for j in range(1, m - 1)))
