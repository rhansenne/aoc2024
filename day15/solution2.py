import copy

ri=rj=0 # robot coordinates
map=[]
moves=[]
deltas={'>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}

def move_box(i,j,dir): # recursively move boxes
    global map
    match(dir):
        case '^':
            if map[i-1][j]=='#' or map[i-1][j+1]=='#':
                return False
            elif map[i-1][j]==']' and map[i-1][j+1]=='[': # two boxes
                map_before_move=copy.deepcopy(map)                
                if not (move_box(i-1,j-1,dir) and move_box(i-1,j+1,dir)):
                    map=map_before_move #undo any moves
                    return False
            elif map[i-1][j]==']' and not move_box(i-1,j-1,dir):
                return False
            elif map[i-1][j]=='[' and not move_box(i-1,j,dir):
                return False
            elif map[i-1][j+1]=='[' and not move_box(i-1,j+1,dir):
                return False                                           
            map[i][j],map[i][j+1]='.','.'            
            map[i-1][j],map[i-1][j+1]='[',']'            
        case 'v':
            if map[i+1][j]=='#' or map[i+1][j+1]=='#':
                return False
            elif map[i+1][j]==']' and map[i+1][j+1]=='[': # two boxes
                map_before_move=copy.deepcopy(map)                
                if not (move_box(i+1,j-1,dir) and move_box(i+1,j+1,dir)):
                    map=map_before_move #undo any moves
                    return False
            elif map[i+1][j]==']' and not move_box(i+1,j-1,dir):
                return False
            elif map[i+1][j]=='[' and not move_box(i+1,j,dir):
                return False
            elif map[i+1][j+1]=='[' and not move_box(i+1,j+1,dir):
                return False                                           
            map[i][j],map[i][j+1]='.','.'            
            map[i+1][j],map[i+1][j+1]='[',']'            
        case '>':
            if map[i][j+2]=='#' or (map[i][j+2]=='[' and not move_box(i,j+2,dir)):
                return False
            map[i][j],map[i][j+1],map[i][j+2]='.','[',']'            
        case '<':
            if map[i][j-1]=='#' or (map[i][j-1]==']' and not move_box(i,j-2,dir)):
                return False
            map[i][j-1],map[i][j],map[i][j+1]='[',']','.'            
    return True
            
def move_robot(i,j,dir):
    global ri,rj
    match(dir):
        case '^':
            if map[i-1][j]=='.' or (map[i-1][j]=='[' and move_box(i-1,j,dir)) or (map[i-1][j]==']' and move_box(i-1,j-1,dir)):
                map[i-1][j],map[i][j]='@','.'
                ri-=1     
        case 'v':
            if map[i+1][j]=='.' or (map[i+1][j]=='[' and move_box(i+1,j,dir)) or (map[i+1][j]==']' and move_box(i+1,j-1,dir)):
                map[i+1][j],map[i][j]='@','.'            
                ri+=1     
        case '>':
            if map[i][j+1]=='.' or (map[i][j+1]=='[' and move_box(i,j+1,dir)):
                map[i][j],map[i][j+1]='.','@'
                rj+=1            
        case '<':
            if map[i][j-1]=='.' or (map[i][j-1]==']' and move_box(i,j-2,dir)):
                map[i][j-1],map[i][j]='@','.'
                rj-=1            

i=0
for l in open('input.txt', 'r').readlines():
    if '#' in l:
        l=l.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')
        map.append([*l.strip()])
        if '@' in l:
            ri,rj=i,l.index('@')
    elif len(l)>1:
        moves+=[*l.strip()]
    i+=1

for m in moves:
    move_robot(ri,rj,m)

sum=0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]=='[':
            sum+=100*i+j
print(sum)