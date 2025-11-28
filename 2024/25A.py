import sys

grids = sys.stdin.read().split("\n\n")
arr = [[list(i) for i in j.splitlines()] for j in grids]
keys, locks = [], []
for i in arr:
    if i[0] == ["."] * 5:
        keys.append([6 - j.index("#") for j in zip(*i)])
    elif i[0] == ["#"] * 5:
        locks.append([j.index(".") - 1 for j in zip(*i)])
print(sum(all(i + j < 6 for i, j in zip(x, y)) for x in keys for y in locks))
