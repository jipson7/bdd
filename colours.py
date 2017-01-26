from solver import Solver, Constraint, Universal

V = {1, 2, 3, 4, 5, 6}  # Vertices

E = [{1, 3}, {2, 3}, {3, 4}, {3, 5}, {2, 5}]  # Edges

E = {frozenset(x) for x in E}

C = {'red', 'blue', 'green', 'yellow'}

solver = Solver()

solver.set_vars(V)

solver.map_to(C)

v_uni = Universal(V, 2)
print(v_uni)

c1 = Constraint()
c1.IN(v_uni, E)

"""
c3 = Constraint()
c3.AND(c1, c2)

c4 = Constraint()
c4.NOT_EQU(v1.mapped, v2.mapped)

c_final = Constraint()
c_final.IMP(c3, c4)

solver.constrain(c_final)

solver.execute()
"""

#Store constraints as strings in a tree like structure? And traverse it?
