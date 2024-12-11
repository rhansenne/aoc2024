stones = [int(d) for d in open('input.txt', 'r').readline().split()]
for c in range(25):
    i=0
    while i < len(stones):
        if stones[i]==0:
            stones[i]=1
        else:
            s=str(stones[i])
            digits=len(s) # faster would be to use math.log10
            d=int(digits/2)
            if digits%2==0:
                stones.insert(i+1, -1)
                stones[i],stones[i+1]=int(s[:d]),int(s[d:])
                i+=1
            else:
                stones[i]*=2024
        i+=1
print(len(stones))