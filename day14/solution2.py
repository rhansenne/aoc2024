import re, numpy as np
np.set_printoptions(threshold=np.inf,linewidth=1000)
w,h=101,103
room=np.zeros([h,w],dtype=int)
robots=[]
for l in open('input.txt', 'r').readlines():
    x,y,vx,vy=(int(c) for c in re.findall('(-*\d+)',l))
    room[y][x]+=1
    robots.append([y,x,vy,vx])
for second in range(1,10000):
    for r in robots:
        room[r[0]][r[1]]-=1
        r[0],r[1]=(r[0]+r[2])%h,(r[1]+r[3])%w
        room[r[0]][r[1]]+=1
    if not 2 in room:
        print(second)
        print(room)
        break