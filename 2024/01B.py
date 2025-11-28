import sys
from collections import Counter

arr = [list(map(int, i.split())) for i in sys.stdin.read().splitlines()]
c = Counter(list(zip(*arr))[1])
print(sum(a * c[a] for a, b in arr))
