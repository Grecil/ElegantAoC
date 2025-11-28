import sys

s = sys.stdin.read()
n = len(s)
arr = []
for i in range(n):
    if i % 2 == 0:
        arr.append(((i // 2), (int(s[i]))))
    else:
        arr.append((".", int(s[i])))
for i in range((n - 1) // 2, -1, -1):
    for j in range(len(arr) - 1, -1, -1):
        if arr[j][0] == i:
            break
    flag = False
    for k in range(j):
        if arr[k][0] == "." and arr[k][1] >= arr[j][1]:
            flag = True
            break
    if flag:
        temp = arr[k]
        arr[k] = arr[j]
        arr[j] = (".", arr[j][1])
        if arr[j][1] != temp[1]:
            arr.insert(k + 1, (".", temp[1] - arr[j][1]))
print(sum(i * j if j != "." else 0 for i, j in enumerate([a for a, b in arr for _ in range(b)])))
