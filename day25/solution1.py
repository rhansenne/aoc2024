keys=[]
locks=[]
for schematic in open('input.txt', 'r').read().split('\n\n'):
    s=[[*l] for l in schematic.split('\n')]    
    num=[0]*len(s[0])
    for i in range(1,len(s)-1):
        for j in range(len(s[0])):
            if s[i][j]=='#':
                num[j]+=1
    if s[0][0]=='#':
        locks.append(num)
    else:
        keys.append(num)
fit=0   
for k in keys:
    for l in locks:
        for i in range(len(k)):
            if k[i]+l[i]>len(s)-2:
                break
            if i==len(k)-1:
                fit+=1
print(fit)
