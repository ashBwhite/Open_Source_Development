import sqlite3
from contextlib import closing

# task 1
con = sqlite3.connect("../wk11/myfile.db")
c = con.cursor()
c.execute('''CREATE TABLE students([student_id] INTEGER PRIMARY KEY , [name] TEXT)''')
c.execute('''CREATE TABLE courses([course_code] INTEGER PRIMARY KEY , [course_name] TEXT)''')
c.execute('''CREATE TABLE grades([student_id] INTEGER, [course_code] INTEGER, [grade_percent] INTEGER)''')

# task 2
c.execute("PRAGMA table_info(students)")
rows = c.fetchall()
for row in rows:
    print(row)

# task 3
insert1 = '''INSERT INTO students[(student_id, name)] VALUES(1, John)'''
insert2 = '''INSERT INTO students[(student_id, name)] VALUES(2, Ji)'''
insert3 = '''INSERT INTO students[(student_id, name)] VALUES(3, Jerry)'''
insert4 = '''INSERT INTO students[(student_id, name)] VALUES(4, Joe)'''
insert5 = '''INSERT INTO students[(student_id, name)] VALUES(5, James)'''


# task 4
query1 = '''INSERT INTO courses(course_code, course_name) VALUES(?, ?)'''
value1 = (1234, "Data_Structure")
query2 = '''INSERT INTO courses(course_code, course_name) VALUES(?, ?)'''
value2 = (2345, "Web_application_development")
query3 = '''INSERT INTO courses(course_code, course_name) VALUES(?, ?)'''
value3 = (3456, "Agile_software_development")
query4 = '''INSERT INTO courses(course_code, course_name) VALUES(?, ?)'''
value4 = (4567, "Open_source_development")
query5 = '''INSERT INTO courses(course_code, course_name) VALUES(?, ?)'''
value5 = (5678, "Data_Structure")

con.execute(query1, value1)
con.execute(query2, value2)
con.execute(query3, value3)
con.execute(query4, value4)
con.execute(query5, value5)

# task 5
grade1 = '''INSERT INTO grades[(student_id, course_code, grade_percent)] VALUES(1, 1234, 68)'''
grade2 = '''INSERT INTO grades[(student_id, course_code, grade_percent)] VALUES(2, 2345, 72)'''
grade3 = '''INSERT INTO grades[(student_id, course_code, grade_percent)] VALUES(3, 4556, 96)'''
grade4 = '''INSERT INTO grades[(student_id, course_code, grade_percent)] VALUES(4, 3456, 59)'''
grade5 = '''INSERT INTO grades[(student_id, course_code, grade_percent)] VALUES(5, 5678, 88)'''

# task 6
delete_row_student = '''DELETE FROM students WHERE student_id = 4'''
delete_row_course = '''DELETE FROM courses WHERE course_code = 2345'''
delete_row_grade = '''DELETE FROM grades WHERE grade_percent = 59'''
c.execute(delete_row_student)
c.execute(delete_row_course)
c.execute(delete_row_grade)

# task 7
student_id = 5
name = 'Daniel'
with closing(con.cursor()) as c:
    sql = '''UPDATE students SET name = ? WHERE student_id = ?'''
    c.execute(sql, (name, student_id))
    con.commit()

course_code = 1234
course_name = 'AI'
with closing(con.cursor()) as c:
    sql = '''UPDATE courses SET course_code = ? WHERE course_name = ?'''
    c.execute(sql, (course_name, course_code))
    con.commit()

# task 8
def print_query(cs, q):
    cs.execute(q)
    result_set = cs.fetchall()
    for row in result_set:
        print(row)
    print()

con = sqlite3.connect("../wk11/myfile.db")
c = con.cursor()
print_query(c, '''SELECT * FROM students''')

# task 9
con = sqlite3.connect("../wk11/myfile.db")
c = con.cursor()
print_query(c, '''SELECT * FROM courses LIMIT 3;''')

# task 10
drop_table = "DROP TABLE grades"
c.execute(drop_table)
