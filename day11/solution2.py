occs={} #occurrences of each number

def inc(s,n):
    if s in occs:
        occs[s]+=n
    else:
        occs[s]=n
        
def dec(s,n):
    if occs[s]>n:
        occs[s]-=n
    else:
        del occs[s]        
        
def expand(s,occ):
    dec(s,occ)
    if s==0:
        inc(1,occ)
    else:
        st=str(s)
        digits=len(st) # faster would be to use math.log10
        if digits%2==0:
            d=int(digits/2)            
            inc(int(st[:d]),occ)
            inc(int(st[d:]),occ)
        else:
            inc(s*2024,occ)

for d in open('input.txt', 'r').readline().split():
    inc(int(d),1)  
for c in range(75):
    oldoccs=occs.copy()
    for s in oldoccs.keys():
        expand(s,oldoccs[s])
print(sum(occs.values()))