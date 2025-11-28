import sys

rules, updates = sys.stdin.read().split("\n\n")
rules = [i.split("|") for i in rules.splitlines()]
updates = [i.split(",") for i in updates.splitlines()]
print(
    sum(
        int(i[len(i) // 2]) if not any(a in i and b in i and i.index(a) > i.index(b) for a, b in rules) else 0
        for i in updates
    )
)
