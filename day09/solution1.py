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
    while disk[firstSpace]>=0:
        firstSpace+=1
    while disk[lastBlock]<0:
        lastBlock-=1
    if firstSpace < lastBlock:
        disk[firstSpace], disk[lastBlock] = disk[lastBlock], disk[firstSpace]

checksum=0
for i in range(0,len(disk)): #calculate checksum
    if disk[i]==-1:
        break
    checksum+=i*disk[i]
print(checksum)