import sys
from math import prod

inp = [i.strip("\n") + " " for i in sys.stdin.readlines()]
ans = 0
for row in map(list, zip(*inp)):
    if all(i == " " for i in row):
        ans += sum(nums) if op == "+" else prod(nums)
        continue
    elif row[-1] in ("+", "*"):
        op = row.pop()
        nums = []
    nums.append(int("".join(row)))
print(ans)
