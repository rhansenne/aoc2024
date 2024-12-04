import numpy as np
ws = np.genfromtxt('input.txt', delimiter=1, dtype='str')
tot=0
for i in range(1,len(ws)-1):
    for j in range(1,len(ws[i])-1):    
        if ws[i][j] == 'A' and \
        ((ws[i-1][j-1] == 'M' and ws[i+1][j+1] == 'S') or (ws[i-1][j-1] == 'S' and ws[i+1][j+1] == 'M')) and \
        ((ws[i+1][j-1] == 'M' and ws[i-1][j+1] == 'S') or (ws[i+1][j-1] == 'S' and ws[i-1][j+1] == 'M')):
            tot+=1
print(tot) 