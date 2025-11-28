import sys
from itertools import combinations

arr = [list(map(int, i.split())) for i in sys.stdin.read().splitlines()]
print(
    sum(
        any(
            all(0 < i[j] - i[j + 1] < 4 for j in range(len(i) - 1))
            or all(-4 < i[j] - i[j + 1] < 0 for j in range(len(i) - 1))
            for i in combinations(k, len(k) - 1)
        )
        for k in arr
    )
)
