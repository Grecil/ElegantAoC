import sys
from collections import defaultdict
from itertools import chain


def swap(a, b):
    pairs.append((a, b))
    for i, (x, n) in enumerate(gates):
        if n in (a, b):
            gates[i] = (x, next(j for j in (a, b) if j != n))


wires, joints = sys.stdin.read().split("\n\n")
wires = {i[:3]: int(i[5]) for i in wires.splitlines()}
gates = [(i.split(), j) for i, j in (k.split(" -> ") for k in joints.splitlines())]
pairs, num_z = [], sum(v.startswith("z") for _, v in gates)
while len(pairs) < 4:
    adder, carry = "", ""
    lookup = {output: (a, op, b) for (a, op, b), output in gates}
    reverse_lookup = defaultdict(str, {frozenset(v): k for k, v in lookup.items()})
    adder = reverse_lookup[frozenset(("x00", "XOR", "y00"))]
    carry = reverse_lookup[frozenset(("x00", "AND", "y00"))]
    for i in range(1, num_z):
        xi, yi, zi = f"x{i:02}", f"y{i:02}", f"z{i:02}"
        bit = reverse_lookup[frozenset((xi, "XOR", yi))]
        adder = reverse_lookup[frozenset((bit, "XOR", carry))]
        if adder:
            c1 = reverse_lookup[frozenset((xi, "AND", yi))]
            c2 = reverse_lookup[frozenset((bit, "AND", carry))]
            carry = reverse_lookup[frozenset((c1, "OR", c2))]
        else:
            a, op, b = lookup[zi]
            swap(bit, next(n for n in (a, b) if n != carry))
            break
        if adder != zi:
            swap(adder, zi)
            break
print(*sorted(chain.from_iterable(pairs)), sep=",")
