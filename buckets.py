from solver import Generator, Block
from functools import reduce

X = 4  # Number of buckets
Y = 4  # Number of unique items
Z = 1  # Bucket Capacity

block_matrix = []

block_values = [True, False]

for i in range(X):
    block_matrix.append([])
    for j in range(Y):
        block_matrix[i].append(Block(block_values))

block_list = reduce(lambda x, y: x+y, block_matrix)

bdd = Generator(block_list)

temp_block = bdd.apply('+', block_matrix[0])

print(temp_block)

# bdd.lte(temp_block, Z)

# solutions = bdd.execute()

# print(solutions)
