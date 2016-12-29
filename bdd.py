__bdd_body__ = """
#include <stdio.h>
#include <vector>
#include "bdd.h"
#include "fdd.h"
#include "bvec.h"
using namespace std;
int main() {{

    bdd_init({node_num}, {cache_size});

    int block_count = {block_count};

    int domains[block_count] = {block_domains};

    fdd_extdomain(domains, block_count);

    bvec *blocks = new bvec[block_count];

    for (int i = 0; i < block_count; i++) {{
        blocks[i] = bvec_varfdd(i);
    }}

    {constraints}

    cout << fddset << constraint << endl;

    long num_solutions = (long)bdd_satcount(constraint);

    cout << "There are " << num_solutions << " solution(s)." << endl;

}}
"""

class BDDException(Exception):
    pass

class Contraints:
    ALL_UNIQUE = 1
    ALL_SATISFIED = 2
    PARTIALLY_SATISFIED = 3

class BDDSolver:

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


if __name__ == "__main__":

    colours = 4
    vertices = 4

    from itertools import combinations
    edges = [set(x) for x in combinations(range(vertices), 2)]

    blocks = []

    #Create the blocks
    for x in range(vertices):
        blocks.append(Block(colours))

    bdd = BDDSolver(blocks)
    bdd.create()

    #Define Contr

