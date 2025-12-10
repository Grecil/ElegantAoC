import sys
from scipy.optimize import linprog
inp=[i.strip().split() for i in sys.stdin.readlines()]
ans=0
for row in inp:
    want=tuple(map(int,row[-1][1:-1].split(",")))
    have=[]
    for i in range(1,len(row)-1):
        temp=[0]*len(want)
        for j in map(int,row[i][1:-1].split(",")):
            temp[j]=1
        have.append(temp)
    ans+=linprog([1]*len(have),A_eq=list(zip(*have)),b_eq=want,integrality=True).fun
print(int(ans))
        