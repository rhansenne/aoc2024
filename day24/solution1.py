inp,logic=open('input.txt', 'r').read().split('\n\n')
inputs={}
rules=[]
zs=set()

for i in inp.split('\n'):
    inputs[i[:3]]=int(i[5])
for l in logic.split('\n'):
    s=l.split(' ')
    in1,op,in2,out=s[0],s[1],s[2],s[4]
    rules.append((in1,op,in2,out))
    if s[4][0]=='z':
        zs.add(s[4])

while not zs.issubset(set(inputs.keys())):
    for r in rules:
        if r[0] in inputs and r[2] in inputs:
            match(r[1]):
                case 'AND':
                    inputs[r[3]]=inputs[r[0]]&inputs[r[2]]
                case 'OR':
                    inputs[r[3]]=inputs[r[0]]|inputs[r[2]]
                case 'XOR':
                    inputs[r[3]]=inputs[r[0]]^inputs[r[2]]
    
out=[inputs['z'+(str(i) if i>9 else ('0'+str(i)))] for i in reversed(range(len(zs)))]
print(int(''.join([str(x) for x in out]),2))             