import math
numeric=[['7','8','9'],['4','5','6'],['1','2','3'],[None,'0','A']]
directional=[[None,'^','A'],['<','v','>']]

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
    return seqs

tot=0
for l in open('input.txt', 'r').readlines():
    code=l.strip()
    codesum=0
    for seqs in solve_bfs(numeric,code,(3,2)):
        min1=math.inf
        for seq in seqs:
            sum1=0
            for seqs2 in solve_bfs(directional,seq,(0,2)):
                min2=math.inf
                for seq2 in seqs2:
                    sum2=sum([len(next(iter(s))) for s in solve_bfs(directional,seq2,(0,2))])
                    min2=min(min2,sum2)
                sum1+=min2
            min1=min(min1,sum1)
        codesum+=min1
    tot+=codesum*int(code[:-1])
print(tot)