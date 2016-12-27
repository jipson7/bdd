from itertools import combinations

class BDDException(Exception):
    pass

class Contraints:
    ALL_UNIQUE = 1
    ALL_SATISFIED = 2
    PARTIALLY_SATISFIED = 3

class BDDSolver:

    blocks = {}
    constraints = []

    def __init__(self, blocks=None):
        if blocks not None:
            self.set_blocks(blocks)

    def set_blocks(self, blocks):
        if type(blocks) == list:
            self.blocks = self._create_keys_(blocks)
        elif type(blocks) == dict:
            self.blocks = blocks
        else:
            raise BDDException("Invalid blocks set")

    def _create_keys_(self, blocks):
        return {i: blocks[i] for i in range(len(blocks))}

    def create(self):
        #TODO print to file

    def execute(self):
        #TODO print to file and run
        self.create()
        pass

class Block:

    potential_vals = []

    def __init__(self, val):
        if type(val) == int:
            self.potential_vals = [x for x in range(val)]
        elif type(val) == list:
            self.potential_vals = val
        else:
            raise BDDException("Invalid block type.")


if __name__ == "__main__":

    colours = 4
    vertices = 4

    edges = [set(x) for x in combinations(range(vertices), 2)]

    blocks = []

    #Create the blocks
    for x in range(vertices):
        blocks.append(Block(colours))

    #Define Contr

