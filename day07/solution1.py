def evaluate(eq):
    if len(eq)==1:
        return [eq[0]]
    return evaluate([eq[0]+eq[1]]+eq[2:]) + evaluate([eq[0]*eq[1]]+eq[2:])

tot=0
for l in open('input.txt', 'r').readlines():
    res=int(l[:l.index(':')])
    eq=[int(i) for i in l[l.strip().index(':')+1:].split()]
    if res in evaluate(eq):
        tot+=res
print(tot)