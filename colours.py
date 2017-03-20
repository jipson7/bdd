from itertools import combinations
from solver import Generator, Block

colours = ['red', 'yellow', 'green', 'blue']
num_v = 4
edges = [list(x) for x in combinations(range(num_v), 2)]

blocks = [Block(colours) for _ in range(num_v)]

bdd = Generator(blocks)

for e in edges:
    bdd.not_equ(blocks[e[0]], blocks[e[1]])

solutions = bdd.execute()

print(len(solutions))
