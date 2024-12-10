import numpy as np
map = np.array([[int(d) for d in l.strip()] for l in open('input.txt', 'r').readlines()])
trailheads = zip(np.where(map==0)[0],np.where(map==0)[1])

paths=set()
def climb(x,y,path):
    global paths    
    if map[x][y] == 9:
        paths.add(tuple(path+[(x,y)]))
        return
    else:
        for nxt in (0,-1),(0,1),(1,0),(-1,0):
            x2,y2=x+nxt[0],y+nxt[1]
            if 0<=x2<len(map) and 0<=y2<len(map[0]) and map[x2][y2]==map[x][y]+1:
                climb(x2,y2,path+[(x2,y2)])
                    
score=0
for t in trailheads:
    paths=set()
    climb(t[0],t[1],[(t[0],t[1])])    
    score+=len(paths)
print(score)