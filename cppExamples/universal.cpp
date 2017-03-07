#include "fdd.h"
#include "bvec.h"

using namespace std;

/**
 * x < 100
 * for all i; i < 5; x mod i == 0
 */

/**
 * Returns the remainder of two numbers
 *
 * Note: I have tested this function in a separate file
 * to confirm that it works, and it does
 */
bvec bvec_mod(bvec number, bvec divisor) {
    bvec d = bvec_coerce(number.bitnum(), divisor);
    bvec result, remainder;
    bvec_div(number, d, result, remainder);
    return remainder;
}

int main() {
    
    bdd_init(1000000, 10000000);

    int domains[2] = {200, 200};

    fdd_extdomain(domains, 2);

    bvec x = bvec_varfdd(0);
    bvec i = bvec_varfdd(1);
    bdd iset = fdd_ithset(1);

    int x_bits = x.bitnum();
    int i_bits = i.bitnum();

    bvec hundred = bvec_con(x_bits, 100);
    bvec five = bvec_con(i_bits, 5);
    bvec two = bvec_con(i_bits, 2);

    bdd c1 = x < hundred;

    bdd c2 = (i < five) & (i >= two);

    bvec mod = bvec_mod(x, i);
    bvec zero = bvec_con(mod.bitnum(), 0);

    bdd c3 = bvec_equ(mod, zero);

    bdd c4 = bdd_imp(c2, c3);

    bdd c = c1 & bdd_forall(c4, iset);


    cout << fddset << c << endl;

    return 0;
}
