from functools import cache
from random import random

numpad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    " ": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}
keypad = {
    " ": (0, 0),
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
xdir = lambda x: "v" if x > 0 else "^"
ydir = lambda x: ">" if x > 0 else "<"


@cache
def moves(curr, new):
    pad = keypad if (new in keypad and curr in keypad) else numpad
    dist = (pad[new][0] - pad[curr][0], pad[new][1] - pad[curr][1])
    ret = xdir(dist[0]) * abs(dist[0]) + ydir(dist[1]) * abs(dist[1])
    if pad[" "] == (pad[new][0], pad[curr][1]):
        return ret[::-1] + "A"
    if pad[" "] == (pad[curr][0], pad[new][1]):
        return ret + "A"
    return (ret if random() < 0.5 else ret[::-1]) + "A"


@cache
def score(seq, depth, curr=0):
    if depth == 0:
        return len(seq)
    for i, key in enumerate(seq):
        curr += score(moves(seq[i - 1], key), depth - 1)
    return curr


sequences = [input() for _ in range(5)]
ans = 0
for seq in sequences:
    temp = float("inf")
    for _ in range(500):
        moves.cache_clear()
        score.cache_clear()
        temp = min(temp, score(seq, 26) * int(seq[:-1]))
    ans += temp
print(ans)
