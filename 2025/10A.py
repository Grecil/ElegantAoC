import sys
from collections import deque
inp=[i.strip().split() for i in sys.stdin.readlines()]
ans=0
for row in inp:
    want=int(row[0][len(row[0])-2:0:-1].replace(".","0").replace("#","1"),2)
    have=[sum(1<<i for i in map(int,row[i][1:-1].split(","))) for i in range(1,len(row)-1)]
    vis=set()
    q=deque([(0,0)])
    while q:
        c,x=q.popleft()
        if x==want:
            ans+=c
            break
        for i in have:
            if x^i not in vis:
                vis.add(x^i)
                q.append((c+1,x^i))
print(ans)
        