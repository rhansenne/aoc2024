from functools import lru_cache 

lst=[l.strip() for l in open('input.txt', 'r').readlines()]
towels=[t.strip() for t in lst[0].split(',')]

@lru_cache
def make(pattern): 
    for t in towels:
        if pattern.startswith(t):
            if pattern==t or make(pattern[len(t):]):
                return True                                    
    return False

possible=0
for i in range(2,len(lst)):
    if make(lst[i]):
        possible+=1
print(possible)