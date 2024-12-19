from functools import lru_cache 

lst=[l.strip() for l in open('input.txt', 'r').readlines()]
towels=[t.strip() for t in lst[0].split(',')]

@lru_cache
def make(pattern):
    if len(pattern)==0:
        return 1
    return sum([make(pattern[len(t):]) for t in towels if pattern.startswith(t)])
    
print(sum([make(lst[i]) for i in range(2,len(lst))]))    