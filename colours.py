from solver import Generator, Block
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Sqlalchemy Setup
"""
engine = create_engine('sqlite:///colours.db')
db = (sessionmaker(bind=engine))()
Base = declarative_base()


class Edge(Base):
    __tablename__ = 'edge'
    v1 = Column(Integer, primary_key=True)
    v2 = Column(Integer, primary_key=True)


class Vertex(Base):
    __tablename__ = 'vertex'
    v = Column(Integer, primary_key=True)


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

for s in solutions:
    print(s)
