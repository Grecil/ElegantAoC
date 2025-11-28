import sys
from itertools import product

ops = [list(product("+*", repeat=i)) for i in range(12)]
arr = sys.stdin.read().splitlines()
ans = 0
for i in arr:
    target, nums = i.split(": ")
    nums = [int(i) for i in nums.split()]
    target = int(target)
    n = len(nums)
    for j in ops[n - 1]:
        curr = nums[0]
        for i in range(n - 1):
            if j[i] == "+":
                curr += nums[i + 1]
            else:
                curr *= nums[i + 1]
            if curr > target:
                break
        if curr == target:
            ans += target
            break
print(ans)
