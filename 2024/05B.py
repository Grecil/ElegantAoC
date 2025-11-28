import sys
from collections import defaultdict

rules, updates = sys.stdin.read().split("\n\n")
rules = [i.split("|") for i in rules.splitlines()]
updates = [i.split(",") for i in updates.splitlines()]
ruledict = defaultdict(set)
for a, b in rules:
    ruledict[a].add(b)
ans = 0
for i in updates:
    if any(a in i and b in i and i.index(a) > i.index(b) for a, b in rules):
        x = set(i)
        y = {j: ruledict[j] & x for j in i}
        i = sorted(y, key=lambda k: len(y[k]), reverse=True)
        ans += int(i[len(i) // 2])
print(ans)
