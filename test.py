from solver import Generator, Block

vals = ['red', 'yellow', 'green', 'blue']

blocks = [Block(4) for _ in range(4)]

bdd = Generator(blocks)

# bdd.map(lambda x: x < 2, blocks[0])
# bdd.equ(blocks[1], blocks[2])
bdd.not_equ(blocks[2], 2)
# bdd.equ(blocks[3], 1)

bdd.lte(bdd.apply('+', blocks), 3)

solutions = bdd.execute()

for s in solutions:
    print(s)
