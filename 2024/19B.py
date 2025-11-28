import sys
from functools import lru_cache

stripes, towels = sys.stdin.read().split("\n\n")
stripes, towels = stripes.split(", "), towels.splitlines()


@lru_cache(None)
def ways(x):
    return 1 if x == "" else sum(ways(x[len(i) :]) for i in stripes if x.startswith(i))


print(sum(ways(i) for i in towels))
