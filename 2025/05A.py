import sys
from itertools import accumulate

ranges, ids = sys.stdin.read().split("\n\n")
ranges = sorted([*map(int, i.split("-"))] for i in ranges.splitlines())
stk = [ranges[0]]
for a, b in ranges[1:]:
    if a <= stk[-1][1]:
        stk[-1][1] = max(stk[-1][1], b)
    else:
        stk.append([a, b])
ids = [*map(int, ids.splitlines())]
st = set(ids)
for a, b in stk:
    st.add(a)
    st.add(b)
v2i = {v: i for i, v in enumerate(sorted(st))}
pre = [0] * (len(v2i) + 1)
for a, b in stk:
    pre[v2i[a]] += 1
    pre[v2i[b] + 1] -= 1
pre = [*accumulate(pre)]
print(sum(pre[v2i[v]] > 0 for v in ids))
