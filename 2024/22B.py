import sys
from collections import defaultdict

arr = [int(i) for i in sys.stdin.read().splitlines()]
prices = []
for i in arr:
    temp = []
    for _ in range(2000):
        i ^= i * 64
        i %= 16777216
        i ^= i // 32
        i %= 16777216
        i ^= i * 2048
        i %= 16777216
        temp.append(i % 10)
    prices.append(temp)

scores = defaultdict(int)

for price in prices:
    seen, unseen = set(), []
    for j in range(4, 2000):
        delta = (
            price[j - 3] - price[j - 4],
            price[j - 2] - price[j - 3],
            price[j - 1] - price[j - 2],
            price[j - 1] - price[j],
        )
        if delta not in seen:
            unseen.append((delta, price[j]))
            seen.add(delta)
    for delta, val in unseen:
        scores[delta] += val
print(max(scores.values()))
