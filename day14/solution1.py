import re
w,h=101,103
q1=q2=q3=q4=0
for l in open('input.txt', 'r').readlines():
    x,y,vx,vy=(int(c) for c in re.findall('(-*\d+)',l))
    print(x,y,vx,vy)
    for i in range(100):
        x=(x+vx)%w
        y=(y+vy)%h
    if x<w//2 and y<h//2:
        q1+=1
    elif x>w//2 and y<h//2:
        q2+=1
    elif x<w//2 and y>h//2:
        q3+=1
    elif x>w//2 and y>h//2:
        q4+=1
print(q1*q2*q3*q4)