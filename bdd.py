from bddsolver import Generator, Block

colours = 4
vertices = 4


# Used for colour map prototype
from itertools import combinations
edges = [list(x) for x in combinations(range(vertices), 2)]

blocks = []

# Create the blocks
for x in range(vertices):
    blocks.append(Block(colours))

bdd = Generator(blocks)

for e in edges:
    bdd.not_equ(blocks[e[0]], blocks[e[1]])

bdd.execute()

