from bddsolver import Generator, Block

colours = 4
vertices = 4


# Used for colour map prototype
# from itertools import combinations
# edges = [set(x) for x in combinations(range(vertices), 2)]

blocks = []

# Create the blocks
for x in range(vertices):
    blocks.append(Block(colours))

bdd = Generator(blocks)

# Block at index 0 cannot be equal to block at index 1
bdd.not_equ(blocks[0], blocks[1])

bdd.execute()

