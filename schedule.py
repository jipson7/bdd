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


sections = db.query(Section).limit(8).all()

tas = db.query(TA).limit(8).all()

blocks = [Block(tas) for _ in sections]

bdd = Generator(blocks)

for i, s in enumerate(sections):
    def no_overlap(ta, s=s):
        if len(ta.restrictions) == 0:
            return True
        for r in ta.restrictions:
            return not (((s.start_time <= r.end_time) and
                        (s.start_time >= r.start_time)) and
                        ((r.start_time <= s.end_time) and
                        (r.start_time >= s.start_time)))
    bdd.filter(no_overlap, blocks[i])


solutions = bdd.execute()

# for solution in solutions:
#     for section, tas in solution.items():
#         for ta in tas:
#             print(ta.ta_name)
#     # break  # remove to print all solutions

print("There are " + str(len(solutions)) + " solution(s).")
