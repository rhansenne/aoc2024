rules=[]
sum=0
for l in open('input.txt', 'r').readlines():
    if '|' in l:
        rules.append(l.strip().split('|'))
    elif ',' in l:        
        ok=True
        pages=l.strip().split(',')
        for r in rules:
            if r[0] in pages and r[1] in pages and pages.index(r[1])<pages.index(r[0]):
                ok=False
                break
        if ok:
            sum+=int(pages[int((len(pages)-1)/2)])
print(sum)