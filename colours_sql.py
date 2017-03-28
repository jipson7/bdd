from solver import Generator, Block
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Sqlalchemy Setup
"""
engine = create_engine('sqlite:///databases/colours.db')
db = (sessionmaker(bind=engine))()
Base = declarative_base()


class Edge(Base):
    __tablename__ = 'edge'
    v1 = Column(Integer, primary_key=True)
    v2 = Column(Integer, primary_key=True)


class Vertex(Base):
    __tablename__ = 'vertex'
    v = Column(Integer, primary_key=True)

class Result(Base):
    __tablename__ = 'result'
    def __init__(self, s_id, v, color):
        self.solution_id = s_id
        self.v = v
        self.color = color
    result_id = Column(Integer, primary_key=True)
    solution_id = Column(Integer)
    v = Column(Integer)
    color = Column(Text)

"""
Run BDD test
"""
colours = ['red', 'yellow', 'green', 'blue']
num_v = db.query(Vertex).count()

blocks = [Block(colours) for _ in range(num_v)]

bdd = Generator(blocks)

for e in db.query(Edge):
    bdd.not_equ(blocks[e.v1], blocks[e.v2])

solutions = bdd.execute()

for solution_id, solution in enumerate(solutions):
    for v, color in solution.items():
        db.add(Result(solution_id, v, color[0]))
db.commit()

