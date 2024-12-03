import re
res=0
with open('input.txt', 'r') as file:
    f = file.read()
l = re.sub('\n', '', f)
l = re.sub('don\'t\(\).*?do\(\)', '', l)
for mul in re.findall('mul\(\d{1,3},\d{1,3}\)',l):
    x=[int(d) for d in re.findall('\d+',mul)]
    res+=x[0]*x[1]
print(res)