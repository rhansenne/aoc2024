def nth_secret(s,n):
    for _ in range(n):
        s^=s*64%16777216
        s^=s//32%16777216
        s^=s*2048%16777216
    return s

print(sum([nth_secret(int(s),2000) for s in open('input.txt', 'r').readlines()]))