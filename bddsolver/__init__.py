class Generator:

    blocks = {}
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
            self.blocks = self._create_keys_(blocks)
        elif type(blocks) == dict:
            self.blocks = blocks
        else:
            raise BDDException("Invalid blocks set")

    def _create_keys_(self, blocks):
        return {i: blocks[i] for i in range(len(blocks))}

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

    def __init__(self, val):
        if type(val) == int:
            self.potential_vals = [x for x in range(val)]
        elif type(val) == list:
            self.potential_vals = val
        else:
            raise BDDException("Invalid block type.")
