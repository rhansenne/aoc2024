import numpy as np

def occs(l):
    return ''.join(l).count("XMAS") + ''.join(l).count("SAMX") 

ws = np.genfromtxt('input.txt', delimiter=1, dtype='str')
tot=0
for l in ws:
    tot+=occs(l)
for l in ws.T:
    tot+=occs(l)
for i in range(0,len(ws)):
    tot+=occs(np.diag(ws,i))
for i in range(1,len(ws)):
    tot+=occs(np.diag(ws,-i))
ws = np.fliplr(ws)    
for i in range(0,len(ws)):
    tot+=occs(np.diag(ws,i))
for i in range(1,len(ws)):
    tot+=occs(np.diag(ws,-i))
print(tot)