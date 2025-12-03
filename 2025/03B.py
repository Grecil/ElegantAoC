import sys

inp = sys.stdin.read().splitlines()
ans = 0
for i in inp:
    arr = []
    for j in range(11, 0, -1):
        arr.append(max(i[:-j]))
        k = i[:-j].index(arr[-1])
        i = i[k + 1 :]
    arr.append(max(i))
    ans += int("".join(arr))
print(ans)
