import sys
from itertools import accumulate

ranges, ids = sys.stdin.read().split("\n\n")
ranges = [[*map(int, i.split("-"))] for i in ranges.splitlines()]
ids = [*map(int, ids.splitlines())]
st = set(ids)
for a, b in ranges:
    st.add(a)
    st.add(b)
v2i = {v: i for i, v in enumerate(sorted(st))}
pre = [0] * (len(v2i) + 1)
for a, b in ranges:
    pre[v2i[a]] += 1
    pre[v2i[b] + 1] -= 1
pre = [*accumulate(pre)]
print(sum(pre[v2i[v]] > 0 for v in ids))
