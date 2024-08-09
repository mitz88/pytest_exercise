import os

import random


itm = ['a','r','t','r','f','g','h','r']
w = random.choice(itm)

itm.pop(itm.index(w))

print(f"{w} from list {itm} of length {len(itm)}")
