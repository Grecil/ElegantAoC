from collections import Counter

c = Counter(int(i) for i in input().split())

for _ in range(25):
    new = Counter()
    for i in c:
        if i == 0:
            new[1] += c[i]
        else:
            s = str(i)
            x = len(s)
            if not x % 2:
                new[int(s[x // 2 :])] += c[i]
                new[int(s[: x // 2])] += c[i]
            else:
                new[i * 2024] += c[i]
    c = new
print(c.total())
