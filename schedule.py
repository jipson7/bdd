import datetime as dt
from solver import Generator, Block
from sqlalchemy import create_engine, Column, Integer, Text, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

"""
Sqlalchemy Setup
"""
engine = create_engine('sqlite:///databases/schedule.db')
db = (sessionmaker(bind=engine))()
Base = declarative_base()


class TA(Base):
    __tablename__ = 'teaching_assistants'
    teaching_assistant_id = Column(Integer, primary_key=True)
    ta_name = Column(Text)
    restrictions = relationship('TA_Restriction')


class TA_Restriction(Base):
    __tablename__ = 'ta_prior_engagements'
    id = Column(Integer, primary_key=True)
    day_of_week = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    teaching_assistant_id = Column(Integer, ForeignKey('teaching_assistants.teaching_assistant_id'))


class Section(Base):
    __tablename__ = 'sections'
    section_id = Column(Integer, primary_key=True)
    day_of_week = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    classroom_id = Column(Integer, ForeignKey('classrooms.classroom_id'))

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(Text)
    prof_name = Column(Text)


class Classroom(Base):
    __tablename__ = 'classrooms'
    classroom_id = Column(Integer, primary_key=True)
    room_number = Column(Text)
    capacity = Column(Integer)


def time_overlap(t1, t2):
    return (t1.start_time <= t2.end_time and t1.start_time >= t2.start_time) \
            or (t2.start_time <= t1.end_time and t2.start_time >= t1.start_time)

sections = db.query(Section).all()

tas = db.query(TA).all()

blocks = [Block(tas) for _ in sections]

bdd = Generator(blocks)

for i, section in enumerate(sections):
    for ta in tas:
        for restriction in ta.restrictions:
            if time_overlap(restriction, section):
                index = tas.index(ta)
                bdd.not_equ(blocks[i], index)


solutions = bdd.execute()

print(solutions)

# Produce all solutions: True
