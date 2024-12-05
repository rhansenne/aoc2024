rules=[]
sum=0
for l in open('input.txt', 'r').readlines():
    if '|' in l:
        rules.append(l.strip().split('|'))
    elif ',' in l:        
        pages=l.strip().split(',')
        resorted=False
        while True:
            sorted=True
            for r in rules:
                if r[0] in pages and r[1] in pages and pages.index(r[1])<pages.index(r[0]):
                    i0, i1 = pages.index(r[0]), pages.index(r[1])
                    pages[i1], pages[i0] = pages[i0], pages[i1]
                    sorted=False
                    resorted=True
            if sorted:
                break
        if resorted:
            sum+=int(pages[int((len(pages)-1)/2)])
print(sum)