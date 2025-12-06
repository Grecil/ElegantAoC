import sys
from math import prod

inp = [i.strip().split() for i in sys.stdin.readlines()]
ans = 0
for row in map(list, zip(*inp)):
    op = row.pop()
    ans += sum(map(int, row)) if op == "+" else prod(map(int, row))
print(ans)
