from datetime import datetime
import faker
from random import randint
import sqlite3


NUMBER_STUDENTS = randint(30, 50)
NUMBER_TEACHERS = randint(3, 5)
NUMBER_GROUPS = 3
NUMBER_ESTIMATES = 20
subjects_list = ["History", "Maths", "Biology", "Geography", "Physics", "Philosophy"]


def create_db():
    with open("school.sql", "r") as f:
        sql = f.read()

    with sqlite3.connect("school.db") as con:
        cur = con.cursor()
        cur.executescript(sql)


def get_data(number_students=NUMBER_STUDENTS, number_teachers=NUMBER_TEACHERS) -> tuple():
    fake_students = []
    fake_teachers = []

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    students = []
    for student in fake_students:
        students.append((student, randint(1, NUMBER_GROUPS)))

    groups = []
    for group in range(1, NUMBER_GROUPS + 1):
        groups.append((group,))

    teachers = []
    for teacher in fake_teachers:
        teachers.append((teacher,))

    subjects = []
    for sub in subjects_list:
        subjects.append((sub, randint(1, NUMBER_TEACHERS)))

    estimates = []
    for std in range(1, NUMBER_STUDENTS + 1):
        days = []
        subj = {}
        for _ in range(0, randint(1, NUMBER_ESTIMATES)):
            day = randint(1, 31)
            days.append(day)
            days.sort()
        for d in days:
            subj.update({d: randint(1, 6)})
        for key, value in subj.items():
            est_date = datetime(2022, 12, key).date()
            estimates.append((std, value, randint(1, 5), est_date))

    return students, groups, teachers, subjects, estimates


def insert_data_to_db(students, groups, teachers, subjects, estimates) -> None:

    with sqlite3.connect("school.db") as con:

        cur = con.cursor()

        sql_to_students = "INSERT INTO students(student_name, group_id) VALUES (?, ?)"
        cur.executemany(sql_to_students, students)

        sql_to_groups = "INSERT INTO groups(group_number) VALUES (?)"
        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = "INSERT INTO teachers(teacher_name) VALUES (?)"
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = "INSERT INTO subjects(subject, teacher_id) VALUES (?, ?)"
        cur.executemany(sql_to_subjects, subjects)

        sql_to_estimates = """INSERT INTO estimates(student_id, subject_id, estimate, date_of)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_estimates, estimates)

        con.commit()


if __name__ == "__main__":
    create_db()
    insert_data_to_db(*get_data())
