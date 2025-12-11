import sys
from collections import defaultdict

inp = [i.strip().split(": ") for i in sys.stdin.readlines()]
adj = defaultdict(list)
for u, v in inp:
    for vi in v.split():
        adj[u].append(vi)
stk = [("you", "")]
ans = 0
while stk:
    u, p = stk.pop()
    for v in adj[u]:
        if v == "out":
            ans += 1
            continue
        if v != p:
            stk.append((v, u))
print(ans)
