import sys
import re

arr = sys.stdin.read()
pattern = r"(?s)(?:(?<=don't\(\)).*?(?=do\(\)|$))|(?:mul\((\d+),(\d+)\))"
print(sum(int(x) * int(y) if x and y else 0 for x, y in re.findall(pattern, arr)))
