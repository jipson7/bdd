from . import exceptions as ex
from . import constraints as co


class Generator:
    """
    Used to generate and run BuDDy file based on given 
    blocks and constraints on said blocks

    Depending on the constraints, the generator will output the 
    possible solutions. A solution is a value assigned to each block
    that satisfies the given constraints.
    """

    blocks = []
    constraints = []

    def __init__(self, blocks=None,
                 node_num=10000000,
                 cache_size=10000000):
        if blocks is not None:
            self.set_blocks(blocks)
        self.node_num = node_num
        self.cache_size = cache_size

    """
    Assign a set of blocks to the Generator,
    based
    """
    def set_blocks(self, blocks):
        if type(blocks) == list:
            self.__add_keys(blocks)
            self.blocks = blocks
        else:
            raise ex.BDDGenerateException("Invalid blocks set")

    """
    Assigns a key to each block to be used in specifying constraints
    """
    def __add_keys(self, blocks):
        for i, block in enumerate(blocks):
            block.set_index(i)

    def add_constraint(self, op, b1=None, b2=None):
        index1 = self.blocks.index(b1)
        index2 = self.blocks.index(b2)

        if index1 != -1 and index2 != -1:
            print("block1 at " + str(index1))
            print("block2 at " + str(index2))
        else:
            print("cant find em")

    def create(self):
        data = {
            'node_num': self.node_num,
            'cache_size': self.cache_size,
            'block_count': len(self.blocks),
            'block_domains': '{4, 4, 4}', #TODO Implement this
            'constraints': 'coolio' #TODO and this 
        }
        from .template import __bdd_body__
        f = __bdd_body__.format(**data)
        print(f)

    def execute(self):
        self.create()
        pass


class Block:
    """
    Set of possible values that BDDSolver can output

    Block can be initialized with a number to indicate
    that many possible values. For instance, passing 4
    indicates that there are 4 possible values, namely
    [0, 1, 2, 3].

    Alternativley a list of possible values can be passed.

    A block is analogous to a bvec in BuDDy, where the possible
    values of the block are mapped to the possible integer
    values of the bvec
    """


    potential_vals = [] # The list of possible values 
    length = 0          # Number of possible values

    """
    The index value is used to specify the block when 
    identifying constraints
    """
    index = None        

    def __init__(self, val):
        if type(val) == int:
            self.potential_vals = [x for x in range(val)]
            self.length = len(self.potential_vals)
        elif type(val) == list:
            self.potential_vals = val
            self.length = len(val)
        else:
            raise ex.BDDGenerateException("Invalid block type.")

    def set_index(self, i):
        self.index = i

    def get_index(self):
        return self.index

    """
    Length in this case represents the number of 
    possible values that the block can represent.
    """
    def __len__(self):
        return self.length
