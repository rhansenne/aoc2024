import math

a=b=c=ip=0
for l in open('input.txt', 'r').readlines():
    if 'A' in l:
        a=int(l[l.index(':')+2:])
    elif 'B' in l:
        b=int(l[l.index(':')+2:])
    elif 'C' in l:
        c=int(l[l.index(':')+2:])
    elif 'Program' in l:
        prog=[int(c) for c in l[l.index(':')+2:].split(',')]

output=''
while ip < len(prog):
    lit=prog[ip+1]
    combo=[0,1,2,3,a,b,c][lit]
    match(prog[ip]):
        case 0:
            a=int(a/math.pow(2,combo))
        case 1:
            b=b^lit
        case 2:
            b=combo%8
        case 3:
            if a!=0:
                ip=lit
                continue
        case 4:
            b^=c
        case 5:
            output+=str(combo%8)+','
        case 6:
            b=int(a/math.pow(2,combo))
        case 7:
            c=int(a/math.pow(2,combo))
    ip+=2
print(output[:-1])