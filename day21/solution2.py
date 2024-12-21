from functools import lru_cache 
import math
numeric=(('7','8','9'),('4','5','6'),('1','2','3'),(None,'0','A'))
directional=((None,'^','A'),('<','v','>'))

@lru_cache
def solve_bfs(keypad,code,start):
    seqs=[] #shortest sequences per character of the code
    queue=[(start[0],start[1],code,0,'')]
    while queue:
        (i,j,code,idx,seq) = queue.pop(0)
        cont=False
        while keypad[i][j]==code[idx]:
            seq+='A'
            if idx<len(seqs):
                seqs[idx].add(seq)
            else:
                seqs.append({seq})                
            idx+=1
            seq=''
            if idx==len(code):
                cont=True
                break
        if cont:
            continue
        if idx<len(seqs) and len(seq)>=len(next(iter(seqs[idx]))):
                continue
        for d,k in {(0,1):'>',(0,-1):'<',(-1,0):'^',(1,0):'v'}.items(): 
            i2,j2=i+d[0],j+d[1]
            if i2<0 or i2>=len(keypad) or j2<0 or j2>=len(keypad[0]) or keypad[i][j]==None:
                continue
            queue.append((i2,j2,code,idx,seq+k))
    for i in range(len(seqs)): # make cacheable
        seqs[i]=tuple(seqs[i])
    return seqs

@lru_cache
def expand_directional(seqs,times):
    if times==1:
        return len(next(iter(seqs)))
    min1=math.inf
    for seq in seqs:
        sum1=0
        for seqs2 in solve_bfs(directional,seq,(0,2)):
            min2=expand_directional(seqs2,times-1)
            sum1+=min2
        min1=min(min1,sum1)
    return min1

tot=0
for l in open('input.txt', 'r').readlines():
    code=l.strip()
    codesum=sum([expand_directional(seqs,26) for seqs in solve_bfs(numeric,code,(3,2))]) # 26 robots
    tot+=codesum * int(code[:-1])
print(tot)