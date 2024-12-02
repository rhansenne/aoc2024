a, b = map(list, zip(*[l.split() for l in open('input.txt', 'r').readlines()]))
a = [int(i) for i in a]
b = [int(i) for i in b]
a.sort()
b.sort()
sumdiffs=0
for i in range(0,len(a)):
    sumdiffs+=abs(a[i]-b[i])
print(sumdiffs)