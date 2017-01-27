from bddsolver import Generator, Block
from itertools import combinations

colours = 4
vertices = 4

edges = [list(x) for x in combinations(range(vertices), 2)]

blocks = [Block(colours) for _ in range(vertices)]

bdd = Generator(blocks)

for e in edges:
    bdd.not_equ(blocks[e[0]], blocks[e[1]])

result = bdd.execute()

print(result)

