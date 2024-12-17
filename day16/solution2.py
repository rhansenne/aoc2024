import math

dir={0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)} #0=east, 1=south, 2=west, 3=north
map=[[*l] for l in open('input.txt', 'r').read().split('\n')]
best=set()

def solve_bfs(i,j): 
    global best
    minscore=math.inf
    min_tile_scores={}
    queue=[(i,j,0,0,set((i,j)))]
    while queue:
        (i,j,d,score,path) = queue.pop(0) 
        if (i,j,d) in min_tile_scores and score > min_tile_scores[(i,j,d)]:
            continue #discard suboptimal subpaths
        min_tile_scores[(i,j,d)] = score    
        queue.append((i,j,(d+1)%4,score+1000,path)) #turn right                       
        queue.append((i,j,(d-1)%4,score+1000,path)) #turn left                       
        i2, j2 = i+dir[d][0], j+dir[d][1] #move forwards 
        if map[i2][j2] == 'E':
                score+=1
                if score<minscore:
                    minscore=min(minscore,score)
                    best=path
                elif score==minscore:
                    best.update(path)
        elif map[i2][j2] == '.':
                path2=path.copy()
                path2.add((i2,j2))
                queue.append((i2,j2,d,score+1,path2))                        
    return len(best)

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]=='S':
            print(solve_bfs(i,j))