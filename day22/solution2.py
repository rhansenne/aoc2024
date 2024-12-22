def get_prices(s):
    prices={} # prices and their sequences
    seq=[None,None,None,None]
    prev_seqs=set()
    for _ in range(2000):
        prev=s
        s^=s*64%16777216
        s^=s//32%16777216
        s^=s*2048%16777216
        price=s%10
        seq.pop(0)
        seq.append(price-prev%10)
        currseq=tuple(seq)
        if not currseq in prev_seqs:
            if price in prices:
                prices[price].add(currseq)
            else:
                prices[price]={currseq}
        prev_seqs.add(currseq)
    return prices

all_prices=[]
sequences=set()
for s in [int(s) for s in open('input.txt', 'r').readlines()]:
    prices=get_prices(s)
    all_prices.append(prices)
    for seqs in prices.values():
        sequences.update(seqs)

max_bananas=0
for seq in sequences:
    bananas=0
    for prices in all_prices:
        for p,seqs in prices.items():
            if seq in seqs:
                bananas+=p
    max_bananas=max(bananas,max_bananas)
print(max_bananas)