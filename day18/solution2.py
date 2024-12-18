maxx=maxy=70
lastvisited=set()

def path_exists(bts):
    global lastvisited
    lastvisited.clear()
    visited=set()
    queue=[(0,0,set())]
    while queue: # BFS search
        (x,y,path) = queue.pop(0)
        if (x,y) in bts:
            continue    
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x==maxx and y==maxy:
            lastvisited=path
            return True
        path.add((x,y))
        if x<maxx:   
            queue.append((x+1,y,path.copy())) #move right                       
        if x>0:   
            queue.append((x-1,y,path.copy())) #move left                       
        if y<maxy:   
            queue.append((x,y+1,path.copy())) #move down                       
        if y>0:   
            queue.append((x,y-1,path.copy())) #move up                       
    return False    

bts=set()
for l in open('input.txt', 'r').readlines():
    bt=tuple(int(c) for c in l.strip().split(','))
    bts.add(bt)
    if len(lastvisited)>0 and not bt in lastvisited:
        continue
    if not path_exists(bts):
        print(bt)
        break