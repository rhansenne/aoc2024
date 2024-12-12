regions = [[*l.strip()] for l in open('input.txt', 'r').readlines()]
processed=set()

def get_region_area_perim(i,j):
    if (i,j) in processed:
        return 0,[]
    processed.add((i,j))
    area=1
    perim=[]
    for nb in (0,-1),(0,1),(1,0),(-1,0):
        x,y=i+nb[0],j+nb[1]
        if x<0 or x>=len(regions) or y<0 or y>=len(regions[0]) or regions[x][y]!= regions[i][j]:
            perim+=[((x,y),nb)]  
        else:
            a,p=get_region_area_perim(x,y)
            area+=a 
            perim+=p
    return area,perim

price=0
for i in range(len(regions)):
    for j in range(len(regions[0])):
        area,perim = get_region_area_perim(i,j)
        pc=perim.copy()
        pc.sort(key=lambda p: p[0][0]) # sort by x co and reduce vertical sides
        for k in range(len(pc)):
            for l in range(k,len(pc)):
                p1,p2=pc[k],pc[l]
                if p1[0][1]==p2[0][1] and p1[0][0]+1==p2[0][0] and p1[1]==p2[1]:
                    perim.remove(p1)
        pc.sort(key=lambda p: p[0][1]) # sort by y co and reduce horizontal sides
        for k in range(len(pc)):
            for l in range(k,len(pc)):
                p1,p2=pc[k],pc[l]
                if p1[0][0]==p2[0][0] and p1[0][1]+1==p2[0][1] and p1[1]==p2[1]:
                    perim.remove(p1)
        price+=area*len(perim)
print(price)