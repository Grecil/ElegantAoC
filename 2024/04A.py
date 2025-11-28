import sys

arr = sys.stdin.read().splitlines()
n, m = len(arr), len(arr[0])
ans = 0
for i in range(n):
    for j in range(m):
        if i < n - 3 and arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j] in ("XMAS", "SAMX"):
            ans += 1
        if j < n - 3 and arr[i][j : j + 4] in ("XMAS", "SAMX"):
            ans += 1
        if i < n - 3 and j < n - 3:
            if arr[i][j] + arr[i + 1][j + 1] + arr[i + 2][j + 2] + arr[i + 3][j + 3] in ("XMAS", "SAMX"):
                ans += 1
            if arr[i + 3][j] + arr[i + 2][j + 1] + arr[i + 1][j + 2] + arr[i][j + 3] in ("XMAS", "SAMX"):
                ans += 1
print(ans)
