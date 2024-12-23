conn={}

def addconn(c1,c2):
    if c1 in conn:
        conn[c1].add(c2)
    else:
        conn[c1]={c2}

for l in open('input.txt', 'r').readlines():
    c1,c2=l.strip().split('-')
    addconn(c1,c2)
    addconn(c2,c1)

triples=set()
for c1,cs1 in conn.items():
    if c1[0]=='t':
        for c2 in cs1:
            cs2=conn[c2]
            for c in cs1.intersection(cs2):
                triples.add(frozenset({c1,c2,c}))
print(len(triples))