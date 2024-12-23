conn={}
clouds=[]

def addconn(c1,c2):
    if c1 in conn:
        conn[c1].add(c2)
    else:
        conn[c1]={c2}

for l in open('input.txt', 'r').readlines():
    c1,c2=l.strip().split('-')
    addconn(c1,c2)
    addconn(c2,c1)
    clouds.append({c1,c2})

maxcloud=set()
for c1,cs1 in conn.items():
    for c in clouds:
        if c.issubset(cs1):
            c.add(c1)
            if len(c)>len(maxcloud):
                maxcloud=c
print(','.join(sorted(maxcloud)))