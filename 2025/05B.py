import sys

ranges, ids = sys.stdin.read().split("\n\n")
ranges = sorted([*map(int, i.split("-"))] for i in ranges.splitlines())
stk = [ranges[0]]
for a, b in ranges[1:]:
    if a <= stk[-1][1]:
        stk[-1][1] = max(stk[-1][1], b)
    else:
        stk.append([a, b])
print(sum(b - a + 1 for a, b in stk))
