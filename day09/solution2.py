disk=[]
isFile=True
id=0
for dm in open('input.txt', 'r').readline():  #explode disk map
    for block in range(int(dm)): 
        if isFile:
            disk+=[id]
        else: 
            disk+=[-1]
    isFile=not isFile
    if isFile:
        id+=1

firstSpace=0
lastBlock=len(disk)-1        
while firstSpace < lastBlock: #move blocks
    moved=False    
    while firstSpace < lastBlock and not moved:
        while disk[firstSpace]>=0:
            firstSpace+=1
        lenSpace=1
        if firstSpace > lastBlock:
            break
        while disk[firstSpace+lenSpace]<0:
            lenSpace+=1
        while disk[lastBlock]<0:
            lastBlock-=1
        lenBlock=1
        while disk[lastBlock-lenBlock]==disk[lastBlock]:
            lenBlock+=1
        if lenBlock<=lenSpace:
            for i in range(lenBlock):
                disk[firstSpace+i], disk[lastBlock-i] = disk[lastBlock-i], disk[firstSpace+i]
            moved=True
        else:
            firstSpace+=lenSpace            
    firstSpace=0
    lastBlock-=lenBlock

checksum=sum([i*disk[i] for i in range(0,len(disk)) if disk[i]>-1])
print(checksum)