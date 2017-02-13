import os


bdd_body = """
#include "bdd.h"
#include "fdd.h"
#include "bvec.h"

using namespace std;

const int block_count = {block_count};

int main() {{

bdd_init({node_num}, {cache_size});

int domains[block_count] = {block_domains};

fdd_extdomain(domains, block_count);

bvec *blocks = new bvec[block_count];

for (int i = 0; i < block_count; i++) {{
    blocks[i] = bvec_varfdd(i);
}}

int max_bits = {max_bits};

{constraints}

fdd_printset(constraint);

}}
"""

base_constraint = 'bdd constraint = bddtrue;' + os.linesep

constraint = 'constraint &= ({});' + os.linesep

block = 'bvec_coerce(max_bits, blocks[{}])'

constant = 'bvec_con(max_bits, {})'
