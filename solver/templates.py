import os


bdd_body = """
#include "bdd.h"
#include "fdd.h"
#include "bvec.h"

using namespace std;

const int block_count = {block_count};

int get_max_bitnum(bvec* blocks) {{
  int max = 0;
  for (int i = 0; i < block_count; i++) {{
      int b = blocks[i].bitnum();
      if (b > max) {{
          max = b;
      }}
  }}
  return max;
}}

int main() {{

bdd_init({node_num}, {cache_size});

int domains[block_count] = {block_domains};

fdd_extdomain(domains, block_count);

bvec *blocks = new bvec[block_count];

for (int i = 0; i < block_count; i++) {{
    blocks[i] = bvec_varfdd(i);
}}

int max_bits = get_max_bitnum(blocks);

std::cout << "max bits: " << get_max_bitnum(blocks) << std::endl;

{constraints}

fdd_printset(constraint);

}}
"""

base_constraint = 'bdd constraint = bddtrue;' + os.linesep

constraint = 'constraint &= ({});' + os.linesep

block = 'blocks[{}]'

bvec_cons = 'bvec_con(max_bits, {})'
