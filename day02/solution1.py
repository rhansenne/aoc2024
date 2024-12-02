safe=0
for rep in [l.split() for l in open('input.txt', 'r').readlines()]:
    rep = [int(i) for i in rep]
    incs = decs = 0
    for i in range(0,len(rep)-1):
        if 0 < rep[i]-rep[i+1] < 4:
            incs+=1
        if 0 < rep[i+1]-rep[i] < 4:
            decs+=1
    if incs==len(rep)-1 or decs==len(rep)-1:
        safe+=1
print(safe)