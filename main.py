import sqlite3
from faker import Faker
import random

fake = Faker()


conn = sqlite3.connect('university_database.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
''')


for i in range(3):
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (fake.word(),))


for i in range(3):
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (fake.name(),))


for i in range(5):
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (fake.word(), random.randint(1, 3)))


for i in range(30):
    group_id = random.randint(1, 3)
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (fake.name(), group_id))
    student_id = cursor.lastrowid

    for subject_id in range(1, 6):
        grade = random.randint(60, 100)
        date_received = fake.date_this_decade()
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)',
                       (student_id, subject_id, grade, date_received))


conn.commit()


conn.close()
