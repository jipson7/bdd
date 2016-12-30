from . import exceptions as ex
from . import constraints as co

class Generator:

    blocks = []
    constraints = []

    def __init__(self, blocks=None, \
            node_num = 10000000, \
            cache_size = 10000000):
        if blocks is not None:
            self.set_blocks(blocks)
        self.node_num = node_num
        self.cache_size = cache_size

    def set_blocks(self, blocks):
        if type(blocks) == list:
            self.__add_keys(blocks)
            self.blocks = blocks
        else:
            raise ex.BDDGenerateException("Invalid blocks set")

    def __add_keys(self, blocks):
        for i, block in enumerate(blocks):
            block.set_index(i)

    def add_constraint(self, op, b1=None, b2=None):
        pass

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
        #TODO print to file and run
        self.create()
        pass

class Block:

    potential_vals = []
    length = 0
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

    def __len__(self):
        return self.length
