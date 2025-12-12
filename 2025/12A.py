import sys
inp=sys.stdin.read().split("\n\n")
grids=inp.pop()
ans=0
for row in grids.splitlines():
    size,freq=row.split(": ")
    a,b=map(int,size.split("x"))
    tot=sum(map(int,freq.split()))
    if tot*9<=a*b:
        ans+=1
print(ans)