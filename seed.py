import random
import psycopg2
import sqlalchemy
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Student, Group, Teacher, Subject, Grade, init_db


engine = create_engine('postgresql://postgres:mysecretpassword@localhost/university_db')
DBSession = sessionmaker(bind=engine)


class UniversityBuilder:
    def __init__(
            self,
            session: Session, 
            students_amount: int,
            groups_amount: int,
            teachers_amount: int,
            subjects_amount: int,
            grades_amount_per_student: int
    ) -> None:
        
        self.session = session
        self.students_amount = students_amount
        self.groups_amount = groups_amount
        self.teachers_amount = teachers_amount
        self.subjects_amount = subjects_amount
        self.grades_amount_per_student = grades_amount_per_student

        self.faker = Faker()
        self.subjects = [
            'Mathematics',
            'Algebra',
            'Geometry',
            'Science',
            'Geography',
            'History',
            'English',
            'Spanish',
            'German',
            'French',
            'Latin',
            'Greek',
            'Arabic',
            'Computer Science',
            'Art',
            'Economics',
            'Music',
            'Drama',
            'Physical Education']

    def generate_university(self):
        self._generate_groups()
        self._generate_teachers()
        self._generate_students()
        self._generate_subjects()
        self._generate_grades()

    def _generate_groups(self):
        for _ in range(self.groups_amount):
            group = Group(name=random.randint(1, 20))

            self.session.add(group)
        self.session.commit()
           
    def _generate_students(self):       
        all_groups = self.session.query(Group).all()

        for _ in range(self.students_amount):
            group_id = random.choice(all_groups).id
            student = Student(name=self.faker.name(), group_id=group_id)

            self.session.add(student)
        self.session.commit()
        
    def _generate_teachers(self):
        for _ in range(self.teachers_amount):
            teacher = Teacher(name=self.faker.name())

            self.session.add(teacher)
        self.session.commit()

    def _generate_subjects(self):
        all_teachers = self.session.query(Teacher).all()

        for _ in range(self.subjects_amount):
            teacher_id = random.choice(all_teachers).id
            subject_name = random.choice(self.subjects)
            
            subject = Subject(name=subject_name, teacher_id=teacher_id)

            self.session.add(subject)
        self.session.commit()

    def _generate_grades(self):
        all_students = self.session.query(Student).all()
        all_subjects = self.session.query(Subject).all()
        
        for student in all_students:
            for _ in range(self.grades_amount_per_student):
                subject_id = random.choice(all_subjects).id
                grade = random.randint(1, 5)
                date = self.faker.date_this_year()
                
                grade = Grade(student_id=student.id, subject_id=subject_id, grade=grade, date=date)

                self.session.add(grade)
        self.session.commit()

def main():

    init_db(engine)
    with DBSession() as session:
        uni_builder = UniversityBuilder(
            session=session, 
            students_amount=50, 
            groups_amount=3, 
            teachers_amount=5, 
            subjects_amount=8, 
            grades_amount_per_student=20
            )
        uni_builder.generate_university()




if __name__ == '__main__':
    main()

