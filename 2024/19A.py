import sys
from functools import lru_cache

stripes, towels = sys.stdin.read().split("\n\n")
stripes, towels = stripes.split(", "), towels.splitlines()


@lru_cache(None)
def possible(x):
    return 1 if x == "" else any(possible(x[len(i) :]) == 1 for i in stripes if x.startswith(i))


print(sum(possible(i) for i in towels))
