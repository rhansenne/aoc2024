import numpy as np

def find(x):
    return tuple([np.where(map==x)[0][0],np.where(map==x)[1][0]])

map = np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])
pos=set()
co=None
while True:
    if '^' in map:
        co = find('^')
        if co[0]-1>=0:
            if map[co[0]-1,co[1]]=='.':
                map[co[0],co[1]]='.'
                map[co[0]-1,co[1]]='^'
            else:
                map[co[0],co[1]]='>'
        else:
            break
    elif '>' in map:
        co = find('>')
        if co[1]+1<len(map[0]):
            if map[co[0],co[1]+1]=='.':
                map[co[0],co[1]]='.'
                map[co[0],co[1]+1]='>'
            else:
                map[co[0],co[1]]='v'
        else:
            break  
    elif 'v' in map:
        co = find('v')
        if co[0]+1<len(map):
            if map[co[0]+1,co[1]]=='.':
                map[co[0],co[1]]='.'
                map[co[0]+1,co[1]]='v'
            else:
                map[co[0],co[1]]='<'
        else:
            break  
    elif '<' in map:
        co = find('<')
        if co[1]-1>=0:
            if map[co[0],co[1]-1]=='.':
                map[co[0],co[1]]='.'
                map[co[0],co[1]-1]='<'
            else:
                map[co[0],co[1]]='^'
        else:
            break
    pos.add(co)
print(len(pos)+1)