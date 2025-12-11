import sys
from collections import defaultdict, deque
from functools import cache


@cache
def dp(u, p, dac, fft):
    ans = 0
    for v in adj[u]:
        if v == "out":
            return dac & fft
        if v != p:
            ans += dp(v, u, dac | (v == "dac"), fft | (v == "fft"))
    return ans


inp = [i.strip().split(": ") for i in sys.stdin.readlines()]
adj = defaultdict(list)
for u, v in inp:
    for vi in v.split():
        adj[u].append(vi)
print(dp("svr", "", 0, 0))
