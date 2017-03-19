from random import randrange
from solver import Generator, Block

"""
Run BDD test
"""
#Linear map definition
colours = ['red', 'yellow']
num_v = 10000;
num_edge = num_v - 1;

blocks = [Block(colours) for _ in range(num_v)]

bdd = Generator(blocks)

current_v = 0
for _ in range(num_edge):
    v1 = current_v
    current_v += 1
    v2 = current_v
    bdd.not_equ(blocks[v1], blocks[v2])

solutions = bdd.execute()

print(len(solutions))

# for s in solutions:
#     print(s)
