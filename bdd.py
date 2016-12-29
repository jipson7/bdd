from bddsolver import Generator, Block

colours = 4
vertices = 4

from itertools import combinations
edges = [set(x) for x in combinations(range(vertices), 2)]

blocks = []

#Create the blocks
for x in range(vertices):
    blocks.append(Block(colours))

bdd = Generator(blocks)
bdd.create()

