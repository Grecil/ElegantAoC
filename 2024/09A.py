import sys

s = sys.stdin.read()
n = len(s)
arr = []
for i in range(n):
    if not i % 2:
        arr.extend([i // 2] * int(s[i]))
    else:
        arr.extend(["."] * (int(s[i])))
i, j = 0, len(arr) - 1
while i < j:
    if arr[i] != ".":
        i += 1
    if arr[j] == ".":
        j -= 1
    if arr[i] == "." and arr[j] != ".":
        arr[i], arr[j] = arr[j], arr[i]
print(sum(i * j if j != "." else 0 for i, j in enumerate(arr)))
