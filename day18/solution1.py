f=open('input.txt', 'r')
maxx=maxy=70
bts=[]
for i in range(1024):
    bts.append([int(c) for c in f.readline().strip().split(',')])
shortestpaths={}
queue=[(0,0,0)]
while queue: # BFS search
    (x,y,dist) = queue.pop(0)
    if [x,y] in bts:
        continue    
    if (x,y) in shortestpaths and dist >= shortestpaths[(x,y)]:
        continue #discard suboptimal subpaths
    shortestpaths[(x,y)] = dist
    if x==maxx and y==maxy:
        continue
    if x<maxx:   
        queue.append((x+1,y,dist+1)) #move right                       
    if x>0:   
        queue.append((x-1,y,dist+1)) #move left                       
    if y<maxy:   
        queue.append((x,y+1,dist+1)) #move down                       
    if y>0:   
        queue.append((x,y-1,dist+1)) #move up                       
print(shortestpaths[maxx,maxy])