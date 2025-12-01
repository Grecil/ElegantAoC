import sys

inp = sys.stdin.read().strip().split()
cur, ans = 50, 0
for i in inp:
    x = int(i[1:])
    if i[0] == "L":
        cur = (cur - x) % 100
    else:
        cur = (cur + x) % 100
    ans += cur == 0
print(ans)
