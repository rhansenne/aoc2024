import sys
sys.setrecursionlimit(2000)

def nth_secret(initial,n):
    if n==0:
        return initial
    nxt=(initial^initial*64)%16777216
    nxt=(nxt^nxt//32)%16777216
    nxt=(nxt^nxt*2048)%16777216
    return nth_secret(nxt,n-1)    

print(sum([nth_secret(int(s),2000) for s in open('input.txt', 'r').readlines()]))