import numpy as np
map = np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])
pos=set()

def exitmap(d,next_d,dx,dy):
    co = tuple([np.where(map==d)[0][0],np.where(map==d)[1][0]])
    pos.add(co)            
    if 0<=co[0]+dx<len(map) and 0<=co[1]+dy<len(map[0]):
        if map[co[0]+dx,co[1]+dy]=='.':
            map[co[0],co[1]]='.'
            map[co[0]+dx,co[1]+dy]=d
        else:
            map[co[0],co[1]]=next_d
        return False
    else:
        return True

while True:
    if '^' in map:
        if exitmap('^','>',-1,0):
            break
    elif '>' in map:
        if exitmap('>','v',0,1):
            break
    elif 'v' in map:
        if exitmap('v','<',1,0):
            break
    elif '<' in map:
        if exitmap('<','^',0,-1):
            break
print(len(pos)+1)