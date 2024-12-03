import re
res=0
for l in open('input.txt', 'r').readlines():
    for mul in re.findall('mul\(\d{1,3},\d{1,3}\)',l):
        x=[int(d) for d in re.findall('\d+',mul)]
        res+=x[0]*x[1]
print(res)