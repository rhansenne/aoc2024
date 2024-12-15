robot=[0,0]
map=[]
moves=[]

def move(i,j,di,dj): # recursively move robot or box
    if map[i+di][j+dj]!='#' and (map[i+di][j+dj]!='O' or move(i+di,j+dj,di,dj)):
        map[i+di][j+dj],map[i][j]=map[i][j],'.'
        return True
    return False

i=ri=rj=0 # robot coordinates
for l in open('input.txt', 'r').readlines():
    if '#' in l:
        map.append([*l.strip()])
        if '@' in l:
            ri,rj=i,l.index('@')
    elif len(l)>1:
        moves+=[*l.strip()]
    i+=1

deltas={'>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}
for m in moves:
    di,dj=deltas[m]
    if move(ri,rj,di,dj):
        ri,rj=ri+di,rj+dj

sum=0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]=='O':
            sum+=100*i+j
print(sum)