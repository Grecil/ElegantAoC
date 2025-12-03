import sys

inp = sys.stdin.read().splitlines()
ans = 0
for i in inp:
    l1 = max(i[:-1])
    l2 = max(i[i.index(l1) + 1 :])
    ans += int(l1 + l2)
print(ans)
