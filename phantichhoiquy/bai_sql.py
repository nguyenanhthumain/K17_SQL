

import sqlite3

# tạo hoặc kết nối database
conn = sqlite3.connect("truong.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS courses")

# tạo bảng students
cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    course_id INTEGER
)
""")

# tạo bảng courses
cursor.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT
)
""")
# dữ liệu students
students_data = [
    (1, "Van A", "May Tinh", 12),
    (2, "Van B", "Kinh Te", 34),
    (3, "Van C", "Toan Tin", None)
]

cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students_data)

# dữ liệu courses
courses_data = [
    (12, "Giai tich"),
    (34, "Thong ke")
]

cursor.executemany("INSERT INTO courses VALUES (?, ?)", courses_data)

conn.commit()


query = """
SELECT students.student_id, students.name, students.class, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.id
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

    