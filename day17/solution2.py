import math

def execute(a,b,c):
    ip=0
    output=[]
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
                output+=[combo%8]
            case 6:
                b=int(a/math.pow(2,combo))
            case 7:
                c=int(a/math.pow(2,combo))
        ip+=2
    return output

a=b=c=0
for l in open('input.txt', 'r').readlines():
    if 'B' in l:
        b=int(l[l.index(':')+2:])
    elif 'C' in l:
        c=int(l[l.index(':')+2:])
    elif 'Program' in l:
        prog=[int(c) for c in l[l.index(':')+2:].split(',')]

# there is likely a more elegant solution by reverse engineering the math, 
# however by examining how the output sequence evolves in function of increasing 
# value of a, it is clear that the sequence expands front to back and we can 
# easily determine when a certain digit will first appears in any 
# later position. 
for i in range(len(prog)):
    x=prog[-i-1]
    j=0
    if i<len(prog)-1:
        while execute(a+j,b,c)[0]!=x:
            j+=1
    else:
        # this leaves just the first value in the sequence: brute force it
        while execute(a+j,b,c)!=prog:
            j+=1
        print(a+j)
        break
    a=(a+j)