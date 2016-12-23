
#include <stdio.h>
#include <math.h> 
#include "bdd.h"
#include "fdd.h"
#include "bvec.h"

using namespace std;

//Number of bits needed to represent x in binary
int num_bits_for_binary(int x) {
    return (int) floor(log2(x)) + 1;
}

int main() {

    int node_num = 1000000;
    int cache_size = 1000000;

    bdd_init(node_num, cache_size);

    int X = 2; //Number of unique items
    int Y = 2; //Number of buckets
    int Z = 1;  //Bucket capacity

    int domains[X*Y];

    fill_n(domains, X*Y, 2); //Fill domains array with const 2

    fdd_extdomain(domains, X*Y);

    //Create Matrix of Bvecs to represent item presence in each
    
    bvec **items = new bvec *[X];
    for (int i=0; i < X; i++) 
        items[i] = new bvec[Y];
    

    for (int i=0; i < X; i++)
        for (int j=0; j < Y; j++)
            items[i][j] = bvec_varfdd(i*Y + j);

    //Create array of Bvecs to represent sizes
    bvec *sizes = new bvec[Y];
    int max_size_bits = num_bits_for_binary(X);

    for (int j=0; j < Y; j++) {
        sizes[j] = bvec_coerce(max_size_bits, items[0][j]);
        for (int i =1; i < X; i++)
            sizes[j] = sizes[j] + bvec_coerce(max_size_bits, items[i][j]);
    }

    //Ensure all sizes are less than Z
    bdd c1 = bddtrue;
    bvec z_cons = bvec_con(max_size_bits, Z);
    for (int j=0; j < Y; j++) {
        c1 &= bvec_lte(sizes[j], z_cons);
    }
    
    //Create array to count number of times each item used
    bvec *counts = new bvec[X];
    int max_count_bits = num_bits_for_binary(Y);

    for(int i=0; i < X; i++) {
        counts[i] = bvec_coerce(max_count_bits, items[i][0]);
        for(int j=1; j < Y; j++)
            counts[i] = counts[i] + bvec_coerce(max_count_bits, items[i][j]);
    }

    //Ensure each item is only used once
    bdd c2 = bddtrue;
    bvec one_cons = bvec_con(max_count_bits, 1);
    for (int i = 0; i < X; i++)
        c2 &= (counts[i] == one_cons);

   
    //Get and print solution
    bdd c = c1 & c2;
    
    cout << fddset << c << endl;

    long num_solutions = (long)bdd_satcount(c);

    cout << "There are " << num_solutions << " solution(s)." << endl;

    return 0;
}
