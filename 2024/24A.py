import sys
from collections import deque
from operator import or_, xor, and_

gates = {"AND": and_, "OR": or_, "XOR": xor}
wires, joints = sys.stdin.read().split("\n\n")
wires = {i[:3]: int(i[5]) for i in wires.splitlines()}
joints = deque([i.split() for i in joints.splitlines()])
while joints:
    w1, g, w2, _, w3 = joints.popleft()
    if w1 in wires and w2 in wires:
        wires[w3] = gates[g](wires[w1], wires[w2])
    else:
        joints.append((w1, g, w2, _, w3))
ans = [str(wires[i]) for i in sorted((j for j in wires if j[0] == "z"), reverse=True)]
print(int("".join(ans), 2))
