## University Database Management System - README.md

This project provides a Python application for managing a university database using SQLAlchemy. It includes functionalities for generating data, querying student information, and retrieving details about subjects, teachers, and grades. Additionally, the schema migrations for this project can be managed using Alembic, a lightweight database migration tool.

### Project Structure

The project consists of three main Python modules:

1. **models.py:** This module defines the database models using SQLAlchemy's declarative base classes. It includes entities like `Student`, `Group`, `Teacher`, `Subject`, and `Grade`, along with their relationships.

2. **seed.py:** This module focuses on populating the database with sample data. It defines a `UniversityBuilder` class that generates students, groups, teachers, subjects, and assigns grades with random values.

3. **my_select.py:** This module contains various functions (`select_1` to `select_10`) that demonstrate different ways to query the university database. Each function showcases a specific query scenario and prints the results.

**Note:** Both `seed.py` and `my_select.py` rely on the `models.py` module for database schema definitions.

### Database Engine Configuration

- Modify the connection string in both `engine` definitions within `seed.py` and `my_select.py` to match your PostgreSQL database credentials (replace `postgres` with your username and `mysecretpassword` with your actual password).

### Running the Project

1. Ensure you have Python and PostgreSQL installed on your system.
2. Install the required libraries:

   ```bash
   pip install sqlalchemy faker psycopg2 alembic
   ```

   Make sure to include `alembic` for database migrations.
3. Update the database connection string in `seed.py` and `my_select.py` as mentioned above.
4. Navigate to the project directory in your terminal and run:

   ```bash
   alembic init <your_alembic_directory_name>
   ```

   Replace `<your_alembic_directory_name>` with a desired name for the Alembic directory (e.g., `alembic`). This command initializes the Alembic configuration for your project.
5. To create the initial database schema based on your models, run:

   ```bash
   alembic upgrade head
   ```

   This creates the database tables based on the schema defined in `models.py`.
6. To populate the database with sample data, run:

   ```bash
   python seed.py
   ```

   This will generate sample data and populate the university database.
7. To execute the example queries, run:

   ```bash
   python my_select.py
   ```

   This will display the results of each query function on the console.

### Database Schema

[![Uni-db-ER-diagram.png](https://i.postimg.cc/D0tpz7dJ/Uni-db-ER-diagram.png)](https://postimg.cc/WqwwWLyT)

### Example Queries

The `my_select.py` module demonstrates various queries:

- **Average Grade per Student (Top 5):** Retrieves students with their average grades in descending order (limited to top 5).
- **Average Grade in a Subject:** Finds the average grade for a specific subject (including students who might not have a grade for that subject).
- **Average Grade per Group in a Subject:** Calculates the average grade for a subject within each group.
- **Overall Average Grade:** Gets the average grade across all subjects and students.
- **Subjects Taught by a Teacher:** Lists all subjects taught by a particular teacher.
- **Students in a Group:** Retrieves a list of students belonging to a specific group (including those without a group assignment).
- **Grades for Students in a Group and Subject:** Fetches grades for students in a specific group for a particular subject.
- **Average Grade per Subject for a Teacher:** Calculates the average grade for each subject taught by a specific teacher (including subjects without grades).
- **Subjects Taken by a Student:** Lists all subjects (including ungraded ones) a student has taken.
- **Grades and Teacher for a Student and Teacher Combination:** Retrieves information about subjects, grades, and teachers for a student based on their name and the teacher's name (including cases where the student might not have a grade for a subject taught by the specified teacher).

This project provides a starting point for managing a university database using SQLAlchemy. You can modify the existing queries and create new ones to suit your specific needs. Additionally, Alembic allows you to manage schema changes over time by creating migration scripts.
