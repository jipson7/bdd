from solver import Solver, Constraint, Universal

V = {1, 2, 3, 4, 5, 6}  # Vertices

E = {{1, 3}, {2, 3}, {3, 4}, {3, 5}, {2, 5}}  # Edges

C = {'red', 'blue', 'green', 'yellow'}

solver = Solver()

solver.set(V)

solver.map_to(C)

v1 = Universal(V)
v2 = Universal(V)
# OR v1 = solver.universal()

"""
Possible also Single, Exists, None?
"""

c1 = Constraint()
c1.NOT_IN({v1, v2}, E)

c2 = Constraint()
c2.NOT_EQU(v1, v2)

c3 = Constraint()
c3.AND(c1, c2)

c4 = Constraint()
c4.NOT_EQU(v1.mapped, v2.mapped)

c_final = Constraint()
c_final.IMP(c3, c4)

solver.constrain(c_final)

solver.execute()
