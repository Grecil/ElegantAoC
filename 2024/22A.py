import sys

arr = [int(i) for i in sys.stdin.read().splitlines()]
ans = 0
for i in arr:
    for _ in range(2000):
        i ^= i * 64
        i %= 16777216
        i ^= i // 32
        i %= 16777216
        i ^= i * 2048
        i %= 16777216
    ans += i
print(ans)
