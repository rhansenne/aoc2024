import re
from sympy.solvers import solve
from sympy.abc import a,b

tokens=0
for l in open('input.txt', 'r').readlines():
    co = re.findall(r"([\d]+)", l)
    if 'A' in l:
        ax,ay=int(co[0]),int(co[1])
    elif 'B' in l:
        bx,by=int(co[0]),int(co[1])
    elif 'P' in l:
        px,py=int(co[0])+10000000000000,int(co[1])+10000000000000
        sol = solve([a*ax+b*bx-px, a*ay+b*by-py], [a, b])
        if sol[a].is_integer and sol[b].is_integer:
            tokens+=3*sol[a]+sol[b]
print(tokens)