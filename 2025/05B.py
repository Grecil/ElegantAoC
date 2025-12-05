import sys

ranges, ids = sys.stdin.read().split("\n\n")
ranges = sorted([*map(int, i.split("-"))] for i in ranges.splitlines())
st = [ranges[0]]
for a, b in ranges[1:]:
    if a <= st[-1][1]:
        st[-1][1] = max(st[-1][1], b)
    else:
        st.append([a, b])
ans = 0
for a, b in st:
    ans += b - a + 1
print(ans)
