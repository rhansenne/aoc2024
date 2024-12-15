import copy

ri=rj=0 # robot coordinates
map=[]
moves=[]

def move_box_vert(i,j,di): # recursively move boxes vertically
    global map
    if map[i+di][j]=='#' or map[i+di][j+1]=='#':
        return False
    elif map[i+di][j]==']' and map[i+di][j+1]=='[': # two boxes
        map_before_move=copy.deepcopy(map)                
        if not (move_box_vert(i+di,j-1,di) and move_box_vert(i+di,j+1,di)):
            map=map_before_move #undo any moves
            return False
    else:
        for dj in (-1,0,1):        
            if map[i+di][j+dj]=='[' and not move_box_vert(i+di,j+dj,di):
                return False
    map[i][j],map[i][j+1]='.','.'            
    map[i+di][j],map[i+di][j+1]='[',']'
    return True              

def move_box(i,j,dir): # recursively move boxes
    global map
    match(dir):
        case '^':
            return move_box_vert(i,j,-1)           
        case 'v':
            return move_box_vert(i,j,1)           
        case '>':
            if map[i][j+2]=='.' or (map[i][j+2]=='[' and move_box(i,j+2,dir)):
                map[i][j],map[i][j+1],map[i][j+2]='.','[',']'  
                return True          
        case '<':
            if map[i][j-1]=='.' or (map[i][j-1]==']' and move_box(i,j-2,dir)):
                map[i][j-1],map[i][j],map[i][j+1]='[',']','.'            
                return True          
    return False
            
def move_robot(i,j,dir):
    global ri,rj,map
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