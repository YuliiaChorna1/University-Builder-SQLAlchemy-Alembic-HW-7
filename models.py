import datetime
import sqlalchemy

from sqlalchemy import DateTime, String, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Mapped, mapped_column, relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    group_id = mapped_column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))
    student_subjects: Mapped[list["Subject"]] = relationship(
        secondary='grades', back_populates='subject_students'
    )

class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    
class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    
class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    teacher_id = mapped_column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    subject_students: Mapped[list["Student"]] = relationship(
        secondary='grades', back_populates='student_subjects'
    )

class Grade(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id = mapped_column(Integer, ForeignKey("students.id"), nullable=False)
    subject_id = mapped_column(Integer, ForeignKey("subjects.id"), nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(), nullable=False)


def init_db(engine):
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine