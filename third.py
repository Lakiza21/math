from random import randint
import itertools

for p in itertools.product("01",repeat=4):
    print(''.join(p))