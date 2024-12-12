regions = [[*l.strip()] for l in open('input.txt', 'r').readlines()]
processed=set()

def get_region_area_perim(i,j):
    if (i,j) in processed:
        return 0,0
    processed.add((i,j))
    area=1
    perim=0
    for nb in (0,-1),(0,1),(1,0),(-1,0):
        x,y=i+nb[0],j+nb[1]
        if x<0 or x>=len(regions) or y<0 or y>=len(regions[0]) or regions[x][y]!= regions[i][j]:
            perim+=1  
        else:
            a,p=get_region_area_perim(x,y)
            area+=a 
            perim+=p
    return area,perim

price=0
for i in range(len(regions)):
    for j in range(len(regions[0])):
        area,perim = get_region_area_perim(i,j)
        price+=area*perim
print(price)