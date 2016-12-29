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


