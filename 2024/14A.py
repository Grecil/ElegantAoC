import sys

arr = [i.split() for i in sys.stdin.read().splitlines()]
q = [[0, 0], [0, 0]]
for p, v in arr:
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))
    x, y = (px + 100 * vx) % 101, (py + 100 * vy) % 103
    if x != 50 and y != 51:
        q[x > 50][y > 51] += 1
print(q[0][0] * q[0][1] * q[1][0] * q[1][1])
