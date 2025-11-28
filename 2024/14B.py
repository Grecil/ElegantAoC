import sys

arr = [i.split() for i in sys.stdin.read().splitlines()]
pos = [list(map(int, p[2:].split(","))) + list(map(int, v[2:].split(","))) for p, v in arr]
for i in range(1, 10000):
    grid = [[" "] * 103 for _ in range(101)]
    for j in pos:
        j[0], j[1] = (j[0] + j[2]) % 101, (j[1] + j[3]) % 103
        grid[j[0]][j[1]] = "#"
    if any("#################################" in "".join(row) for row in grid):
        print(i)
        break
