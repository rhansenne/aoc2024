map=[[*l] for l in open('input.txt', 'r').read().split('\n')]
minsavings=100

def nocheat_times(i,j):
    times={(i,j):0}
    t=0
    while True:
        t+=1
        for d in {(0,1),(0,-1),(-1,0),(1,0)}: 
            i2,j2=i+d[0],j+d[1]
            if map[i2][j2]=='E':
                times[(i2,j2)]=t
                return times
            elif map[i2][j2]=='.' and (i2,j2) not in times.keys():
                times[(i2,j2)]=t
                i,j=i2,j2
                break

def solve_bfs(i,j):
    times=nocheat_times(i,j)
    queue=[(i,j,0,False,(-1,-1))]
    count=0
    while queue:
        (i,j,time,cheated,prev) = queue.pop(0)
        if cheated and map[i][j]!='#':
            if time <= times[(i,j)]-minsavings:
                count+=1
            continue
        for d in {(0,1),(0,-1),(-1,0),(1,0)}: 
            i2,j2,cheated2=i+d[0],j+d[1],cheated
            if (i2,j2)==prev or i2<0 or i2>=len(map) or j2<0 or j2>=len(map[0]) or (cheated and map[i2][j2]=='#'):
                continue
            if map[i2][j2]=='#':
                cheated2=True
            queue.append((i2,j2,time+1,cheated2,(i,j)))
    return count

i,j=[(x,y) for x in range(len(map)) for y in range(len(map[0])) if map[x][y]=='S'][0]
print(solve_bfs(i,j))