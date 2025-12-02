import sys
from itertools import accumulate
from bisect import bisect_left, bisect_right

nums = [int(2 * str(i)) for i in range(1, 10**6)]
pref = [0, *accumulate(nums)]
inp = sys.stdin.read().split(",")
ans = 0
for i in inp:
    a, b = map(int, i.split("-"))
    pos1 = bisect_left(nums, a)
    pos2 = bisect_right(nums, b)
    ans += pref[pos2] - pref[pos1]
print(ans)
