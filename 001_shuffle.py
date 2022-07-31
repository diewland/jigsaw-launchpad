from pprint import pprint as pp
from random import shuffle

def debug(items, col_size=10):
    def chunker(seq, size): # https://stackoverflow.com/a/434328/466693
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))
    for chk in chunker(items, col_size):
        print(''.join(chk))

# prepare data
items = (['C']*44) + (['R']*5) + (['S']*1)

# suffle 16 times
for rnd in range(0, 16):
    shuffle(items)
    preview = ''.join(items)
    print('round #{:02d} -> {}'.format(rnd, preview))
