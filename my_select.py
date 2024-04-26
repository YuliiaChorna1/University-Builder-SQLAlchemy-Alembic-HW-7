
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker, Session
from models import Student, Group, Teacher, Subject, Grade, init_db


engine = create_engine('postgresql://postgres:mysecretpassword@localhost/university_db')
DBSession = sessionmaker(bind=engine)

def select_1():
    with DBSession() as session:
        students = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
            .select_from(Grade)\
                .join(Student)\
                    .group_by(Student.id)\
                        .order_by(desc('avg_grade'))\
                            .limit(5).all()
        
        print("Query 1 -------------------------------------")
        for student in students:
            print(f"student_name: {student.name} | avg_grade: {student.avg_grade}")

def select_2(subject_name):
    with DBSession() as session:
        result = session.query(Student.name.label("student_name"), func.round(func.avg(Grade.grade), 2).label("avg_grade"), Subject.name.label("subject"))\
            .join(Student)\
                .join(Subject).filter(Subject.name == subject_name)\
                    .group_by(Student.name, Subject.name)\
                        .order_by(desc("avg_grade"))\
                            .limit(1).first()
        
        print("Query 2 -------------------------------------")
        print(f"student_name: {result.student_name} | avg_grade: {result.avg_grade} | subject: {result.subject}")

def select_3(subject_name):  
    with DBSession() as session:
        results = session.query(Group.name.label("group_name"), func.round(func.avg(Grade.grade), 2).label("avg_grade"), Subject.name.label("subject"))\
            .select_from(Grade)\
                .join(Student)\
                    .join(Subject)\
                        .join(Group).filter(Subject.name == subject_name)\
                            .group_by(Group.name, Subject.name)\
                                .order_by(Group.name).all()
        
        print("Query 3 -------------------------------------")
        for group in results:
            print(f"group_name: {group.group_name} | avg_grade: {group.avg_grade} | subject: {group.subject}")

def select_4():  
    with DBSession() as session:
        result = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
            .select_from(Grade).first()
        
        print("Query 4 -------------------------------------")
        print(f"avg_grade: {result.avg_grade}")

def select_5(teacher_name):  
    with DBSession() as session:
        results = session.query(Teacher.name.label("teacher_name"), Subject.name.label("subjects"))\
            .join(Subject)\
                .filter(Teacher.name == teacher_name).all()
        
        print("Query 5 -------------------------------------")
        for subject in results:
            print(f"teacher_name: {subject.teacher_name} | subject: {subject.subjects}")

def select_6(group_name):  
    with DBSession() as session:
        results = session.query(Group.name.label("group_name"), Student.name.label("student_name"))\
            .join(Group, isouter=True)\
                .filter(Group.name == group_name).all()
        
        print("Query 6 -------------------------------------")
        for student in results:
            print(f"group_name: {student.group_name} | student_name: {student.student_name}")

def select_7(group_name, subject_name):  
    with DBSession() as session:
        results = session.query(Student.name.label("student_name"), Grade.grade, Group.name.label("group_name"), Subject.name.label("subject"))\
            .join(Subject)\
                .join(Student)\
                    .join(Group).filter(Group.name == group_name, Subject.name == subject_name).all()
        
        print("Query 7 -------------------------------------")
        for student in results:
            print(f"student_name: {student.student_name} | grade: {student.grade} | group_name: {student.group_name} | subject_name: {student.subject}")

def select_8(teacher_name):  
    with DBSession() as session:
        results = session.query(Teacher.name.label("teacher"), Subject.name.label("subject"), func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
            .join(Teacher, isouter=True)\
                .join(Grade, isouter=True).filter(Teacher.name == teacher_name)\
                    .group_by(Subject.name, Teacher.name).all()
        
        print("Query 8 -------------------------------------")
        for subject in results:
            print(f"teacher_name: {subject.teacher} | subject: {subject.subject} | avg_grade: {subject.avg_grade}")

def select_9(student_name):  
    with DBSession() as session:
        results = session.query(Student.name.label("student_name"), Subject.name.label("subject"))\
            .select_from(Student)\
                .distinct(Subject.name)\
                    .join(Grade, isouter=True)\
                        .join(Subject, isouter=True).filter(Student.name == student_name).all()
        
        print("Query 9 -------------------------------------")
        for subject in results:
            print(f"student_name: {subject.student_name} | subject: {subject.subject}")

def select_10(student_name, teacher_name):  
    with DBSession() as session:
        results = session.query(Student.name.label("student_name"), Subject.name.label("subject"), Teacher.name.label("teacher"), Grade.grade)\
            .select_from(Subject)\
                .join(Grade, isouter=True)\
                    .join(Student, isouter=True)\
                        .join(Teacher, isouter=True)\
                            .filter(Student.name == student_name, Teacher.name == teacher_name).all()
        
        print("Query 10 -------------------------------------")
        for subject in results:
            print(f"student_name: {subject.student_name} | subject: {subject.subject} | teacher_name: {subject.teacher}")

def main():

    init_db(engine)
    select_1()
    select_2(subject_name='Greek')
    select_3(subject_name='Arabic')
    select_4()
    select_5(teacher_name='Debra Daniels')
    select_6(group_name='2')
    select_7(group_name='2', subject_name='French')
    select_8(teacher_name='Debra Daniels')
    select_9(student_name='Heather Smith')
    select_10(student_name='Heather Smith', teacher_name='Debra Daniels')



if __name__ == '__main__':
    main()
