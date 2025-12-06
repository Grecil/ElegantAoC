import sys
from math import prod

inp = [i.strip("\n") for i in sys.stdin.readlines()]
lens = [max(map(len, i)) for i in zip(*[i.split() for i in inp])]
arr = []
for row in inp:
    temp, i = [], 0
    for j in lens:
        temp.append(row[i : i + j])
        i += j + 1
    arr.append(temp)
ans = 0
for row in map(list, zip(*arr)):
    op = row.pop()
    nums = [int("".join(i)) for i in zip(*row)]
    ans += sum(nums) if op[0] == "+" else prod(nums)
print(ans)
