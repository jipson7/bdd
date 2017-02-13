from solver import Generator, Block
from functools import reduce

X = 4  # Number of buckets
Y = 4  # Number of unique items
Z = 1  # Bucket Capacity

block_matrix = []

block_values = [False, True]

for i in range(X):
    block_matrix.append([])
    for j in range(Y):
        block_matrix[i].append(Block(block_values))

# Flatten the block matrix to pass it to Generator
block_list = reduce(lambda x, y: x+y, block_matrix)
bdd = Generator(block_list)

# Restrict Buckets to Capacity
for i in range(X):
    row = block_matrix[i]
    temp_block = bdd.apply('+', row)
    bdd.lte(temp_block, Z)

#Restrict item placement to 1
for i in range(Y):
    column = [row[i] for row in block_matrix]
    temp_block = bdd.apply('+', column)
    bdd.equ(temp_block, 1)

solutions = bdd.execute()
for s in solutions:
    print(s)

print("There are " + str(len(solutions)) + " solution(s).")
