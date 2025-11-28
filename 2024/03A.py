import sys
import re

arr = sys.stdin.read()
pattern = r"mul\((\d+),(\d+)\)"
print(sum(int(x) * int(y) for x, y in re.findall(pattern, arr)))
