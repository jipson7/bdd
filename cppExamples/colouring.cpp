
#include <stdio.h>
#include <vector>
#include <map>
#include "bdd.h"
#include "fdd.h"
#include "bvec.h"

using namespace std;

const int NUM_COLOURS = 4;

const int NUM_VERTICES = 4;

const map<int, vector<int> > graph {
    { 0, { 1, 2, 3 } },
    { 1, { 0, 2, 3 } },
    { 2, { 0, 1, 3 } },
    { 3, { 0, 1, 2 } }
};

int main() {

    int node_num = 1000000;
    int cache_size = 1000000;

    bdd_init(node_num, cache_size);

    int domains[NUM_VERTICES];

    fill_n(domains, NUM_VERTICES, NUM_COLOURS);

    fdd_extdomain(domains, NUM_VERTICES);

    bvec *colours = new bvec[NUM_VERTICES];

    for (int i = 0; i < NUM_VERTICES; i++)
        colours[i] = bvec_varfdd(i);

    bdd constraint = bddtrue;

	for(auto i = graph.begin(); i != graph.end(); ++i) {
		int vertex = i->first;
		vector<int> neighbours = i->second;

        for (auto & n: neighbours) {
            constraint &= (colours[vertex] != colours[n]);
        }
	}

    cout << fddset << constraint << endl;

    long num_solutions = (long)bdd_satcount(constraint);

    cout << "There are " << num_solutions << " solution(s)." << endl;
}
