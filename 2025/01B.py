import sys

inp = sys.stdin.read().strip().split()
cur, ans = 50, 0
for i in inp:
    x = int(i[1:])
    if i[0] == "L":
        if cur - x <= 0:
            ans += abs(cur - x) // 100 + (cur != 0)
        cur = (cur - x) % 100
    else:
        if cur + x > 99:
            ans += (cur + x) // 100
        cur = (cur + x) % 100
print(ans)
