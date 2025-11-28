import sys

arr, moves = sys.stdin.read().split("\n\n")
moves = moves.replace("\n", "")
arr = arr.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")
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
    to_move = [(x, y)]
    flag = True
    for i, j in to_move:
        nx, ny = i + dx, j + dy
        if (nx, ny) not in to_move:
            if grid[nx][ny] == "#":
                flag = False
                break
            elif grid[nx][ny] == "[":
                to_move.extend([(nx, ny), (nx, ny + 1)])
            if grid[nx][ny] == "]":
                to_move.extend([(nx, ny), (nx, ny - 1)])
    if flag:
        for i, j in to_move[::-1]:
            grid[i + dx][j + dy], grid[i][j] = grid[i][j], grid[i + dx][j + dy]
        x, y = x + dx, y + dy
print(sum(100 * i + j if grid[i][j] == "[" else 0 for i in range(1, n - 1) for j in range(1, m - 1)))
