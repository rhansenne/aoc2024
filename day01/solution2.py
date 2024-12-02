a, b = map(list, zip(*[l.split() for l in open('input.txt', 'r').readlines()]))
simil=0
for i in a:
    simil+=int(i)*b.count(i)
print(simil)