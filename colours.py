from solver import Solver, Universal, In, And, Imp

V = {1, 2, 3, 4, 5, 6}  # Vertices

E = [{1, 3}, {2, 3}, {3, 4}, {3, 5}, {2, 5}]  # Edges

E = {frozenset(x) for x in E}

C = {'red', 'blue', 'green', 'yellow'}

solver = Solver()

solver.set_vars(V)

solver.map_to(C)

c1 = Universal(V, lambda v1, v2: v1 != v2)

c2 = Universal(V, lambda v1, v2: True)

c3 = In(c2, E)

c4 = And(c1, c3)
print(str(c4.get()))

c5 = Imp(c4, lambda x, y: x != y)


"""
c4 = Constraint()
c4.NOT_EQU(v1.mapped, v2.mapped)

c_final = Constraint()
c_final.IMP(c3, c4)

solver.constrain(c_final)

solver.execute()
"""

#Store constraints as strings in a tree like structure? And traverse it?
