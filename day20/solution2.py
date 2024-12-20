map=[[*l] for l in open('input.txt', 'r').read().split('\n')]
minsavings=100

def nocheat_times(i,j):
    times={}
    t=0
    while True:
        times[(i,j)]=t
        if map[i][j]=='E':
            return times
        t+=1
        map[i][j]='#'
        for d in {(0,1),(0,-1),(-1,0),(1,0)}:             
            if map[i+d[0]][j+d[1]]!='#':
                i,j=i+d[0],j+d[1]
                break

i,j=[(x,y) for x in range(len(map)) for y in range(len(map[0])) if map[x][y]=='S'][0]
times = nocheat_times(i,j)
path=list(times.keys())
count=0
for k in range(len(path)):
    for l in range(k+1,len(path)):
        p1,p2=path[k],path[l]
        nocheat_dist=abs(times[p2]-times[p1])
        cheat_dist=abs(p2[0]-p1[0])+abs(p2[1]-p1[1])
        if cheat_dist <= 20 and nocheat_dist-cheat_dist>=minsavings:
            count+=1
print(count)