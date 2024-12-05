rules=[]
sum=0
for l in open('input.txt', 'r').readlines():
    if '|' in l:
        rules.append(l.strip().split('|'))
    elif ',' in l:        
        pages=l.strip().split(',')
        ok=True
        for r in rules:
            if r[0] in pages and r[1] in pages and pages.index(r[1])<pages.index(r[0]):
                ok=False
                break
        if not ok:
            while not ok:
                ok=True
                for r in rules:
                    if r[0] in pages and r[1] in pages and pages.index(r[1])<pages.index(r[0]):
                        ok=False
                        i0, i1 = pages.index(r[0]), pages.index(r[1])
                        pages[i1], pages[i0] = pages[i0], pages[i1]
            sum+=int(pages[int((len(pages)-1)/2)])
print(sum)