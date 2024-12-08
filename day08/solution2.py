import itertools

# find coordinates of all antennas
antennas={}
i=0
for l in open('input.txt', 'r').readlines(): 
    j=0
    for c in l:
        if l[j].isalnum():
            if l[j] in antennas:
                antennas[l[j]]+=[(i,j)]
            else:
                antennas[l[j]]=[(i,j)]
        j+=1
    i+=1

# for each pair of antennas determine antinodes in range
antinodes=set()
for a in antennas.values():
    for pair in itertools.combinations(a,2):
        xmin = min(pair[0][0],pair[1][0])
        xmax = max(pair[0][0],pair[1][0])
        ymin = min(pair[0][1],pair[1][1])
        ymax = max(pair[0][1],pair[1][1])
        for d in range(0,max(i,j)):
            x1=xmin-d*(xmax-xmin)
            x2=xmax+d*(xmax-xmin)
            if pair[0][1] <= pair[1][1]:
                y1=ymin-d*(ymax-ymin)
                y2=ymax+d*(ymax-ymin)
            else:
                y1=ymax+d*(ymax-ymin)
                y2=ymin-d*(ymax-ymin)
            if 0<=x1<i and 0<=y1<j:
                antinodes.add((x1,y1))
            if 0<=x2<i and 0<=y2<j:
                antinodes.add((x2,y2))
print(len(antinodes))