# very slow and naive implementation, but works
import numpy as np
import copy
init_map = np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])
pos={}
d=start_d='^' #initial direction
start_pos=np.where(init_map==d) 
co=start_co=tuple([start_pos[0][0],start_pos[1][0]]) #initial coordinates

def exitmap(map,next_d,dx,dy): #next_d:next direction in case of obstruction, dx/dy:coordinate modification in case of forwards move
    global co, d
    if co in pos:
        if d in pos[co]:
            return False, True #loop
        pos[co]+=[d]
    else:            
        pos[co]=[d]
    if 0<=co[0]+dx<len(map) and 0<=co[1]+dy<len(map[0]):
        if map[co[0]+dx,co[1]+dy]=='.':
            map[co[0],co[1]]='.'
            co=tuple([co[0]+dx,co[1]+dy])
            map[co[0],co[1]]=d            
        else:
            d=next_d
            map[co[0],co[1]]=d
        return False, False #tbd
    else:
        return True, False #exit
    
def isloop(map):
    next={'^':['>',-1,0], '>':['v',0,1], 'v':['<',1,0], '<':['^',0,-1]}
    while True:
        exit,loop=exitmap(map,*next[d])
        if exit:
            return False
        if loop:
            return True
                      
altmap=copy.deepcopy(init_map)          
isloop(altmap) #populate guard path in pos
obstruction_pos=pos.copy()
loopmaps=0
i=1
for p in obstruction_pos: #try obstruction at every position on path
    print('checking variation',i,'of',len(obstruction_pos),'for loops')
    i+=1 
    if init_map[p[0],p[1]]=='.':
        altmap=copy.deepcopy(init_map)
        altmap[p[0],p[1]]='#' #place obstruction
        pos={}
        co=start_co
        d=start_d
        if isloop(altmap):
            loopmaps+=1            
print(loopmaps)