import os
from . import templates
from . import exceptions as ex


class Generator:
    """
    Used to generate and run BuDDy file based on given 
    blocks and constraints on said blocks

    Depending on the constraints, the generator will output the 
    possible solutions. A solution is a value assigned to each block
    that satisfies the given constraints.
    """

    blocks = []

    """
    List of constraints imposed upon the blocks.
    """
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
            self.blocks = blocks
        else:
            raise ex.BDDGenerateException("Invalid blocks set")

    """
    Create a string representation of the C++ Buddy implementation
    of the problem as described by the blocks and constraints
    """
    def create(self):
        data = {
            'node_num': self.node_num,
            'cache_size': self.cache_size,
            'block_count': len(self.blocks),
            'block_domains': self.__set_block_domains(),
            'constraints': self.__set_constraints()
        }
        return templates.bdd_body.format(**data)

    """
    Create a the C array of length of blocks to be used for
    allocation in the BuDDy program
    """
    def __set_block_domains(self):
        lengths = [str(len(x)) for x in self.blocks]
        return '{' + ', '.join(lengths) + '}'

    def __set_constraints(self):
        return templates.base_constraint \
                + os.linesep.join(self.constraints)

    def execute(self):
        buddy_file = self.create()
        print(buddy_file)

    def not_equ(self, block1, block2):
        index1 = self.__get_block_index(block1)
        index2 = self.__get_block_index(block2)
        constraint = templates.not_equ.format(index1, index2)
        self.constraints.append(constraint)
        
    def equ(self, block1, block2):
        pass

    def gt(self, block1, block2):
        pass

    def gte(self, block1, block2):
        pass

    def all_unique(self):
        pass

    def partial(self):
        pass

    def __get_block_index(self, block):
        try:
            return self.blocks.index(block)
        except ValueError:
            raise ex.BDDConstraintException('Requested block cannot be found')
            


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

    potential_vals = []  # The list of possible values 
    length = 0           # Number of possible values

    def __init__(self, val):
        if type(val) == int:
            self.potential_vals = [x for x in range(val)]
            self.length = len(self.potential_vals)
        elif type(val) == list:
            self.potential_vals = val
            self.length = len(val)
        else:
            raise ex.BDDGenerateException("Invalid block type.")

    """
    Length in this case represents the number of 
    possible values that the block can represent.
    """
    def __len__(self):
        return self.length


