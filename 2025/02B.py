import sys
from itertools import accumulate
from bisect import bisect_left, bisect_right

st = set()
for i in range(1, 10**6):
    si = str(i)
    j = 2
    while j * len(si) <= 10:
        st.add(int(j * si))
        j += 1
nums = sorted(st)
pref = [0, *accumulate(nums)]
inp = sys.stdin.read().split(",")
ans = 0
for i in inp:
    a, b = map(int, i.split("-"))
    pos1 = bisect_left(nums, a)
    pos2 = bisect_right(nums, b)
    ans += pref[pos2] - pref[pos1]
print(ans)
