import sqlite3

# Connect database
conn = sqlite3.connect('database.db')

# Create cursor
cur = conn.cursor()

# =========================
# CREATE TABLES
# =========================

sql1 = """
create table if not exists student(
id integer primary key autoincrement,
name varchar(50),
branch varchar(20),
city varchar(50)
)
"""

sql2 = """
create table if not exists teacher(
id integer primary key autoincrement,
name varchar(50),
subject varchar(50),
city varchar(50)
)
"""

sql3 = """
create table if not exists course(
id integer primary key autoincrement,
course_name varchar(50)
)
"""

# Execute table queries
conn.execute(sql1)
conn.execute(sql2)
conn.execute(sql3)

print("All Tables created successfully")


# =========================
# REMOVE OLD DATA
# (Avoid Duplicate Entries)
# =========================

conn.execute("delete from student")
conn.execute("delete from teacher")
conn.execute("delete from course")

print("Old records deleted successfully")


# =========================
# INSERT RECORDS
# =========================

sql1 = """
insert into student(name,branch,city)
values
("Keshav","CSE","Delhi"),
("Vivek","CSE","Alwar"),
("Nidhi","EE","Jaipur"),
("Priya","AI","Alwar"),
("Neha","IT","Kota")
"""

sql2 = """
insert into teacher(name,subject,city)
values
("Raunak Goswami","English","Alwar"),
("Dr.Rishi Vyas","Engineering Physics","Jaipur"),
("Neeraj Garg","CS-Fundamentals","Kota"),
("Mani Buttwal","DSA","Bhopal"),
("Dr.Shreya","Computer Network","Jaipur")
"""

sql3 = """
insert into course(course_name)
values
("Database"),
("Fundamentals of AI"),
("Basics of Computer Networks"),
("DSA"),
("Discrete Mathematics and Linear Algebra")
"""

# Execute insert queries
conn.execute(sql1)
conn.execute(sql2)
conn.execute(sql3)

print("Records inserted successfully")


# =========================
# SELECT OPERATIONS
# =========================

print("\nStudents Ordered By Name")

q1 = "select * from student order by name"

cur.execute(q1)

data = cur.fetchall()

for row in data:
    print(row)


print("\nTeachers Starting With Dr.")

q2 = "select * from teacher where name like 'Dr.%'"

cur.execute(q2)

data = cur.fetchall()

for row in data:
    print(row)


print("\nTotal Students")

q3 = "select count(*) from student"

cur.execute(q3)

data = cur.fetchall()

for row in data:
    print(row)


# =========================
# UPDATE OPERATION
# =========================

q4 = """
update student
set city = 'Mumbai'
where name = 'Vivek'
"""

conn.execute(q4)

print("\nStudent record updated successfully")


# =========================
# DELETE OPERATION
# =========================

q5 = """
delete from student
where name = 'Neha'
"""

conn.execute(q5)

print("Student record deleted successfully")


# =========================
# FINAL DATA
# =========================

print("\nFinal Student Table")

cur.execute("select * from student")

data = cur.fetchall()

for row in data:
    print(row)


# Save changes
conn.commit()

# Close connection
conn.close()

print("\nDatabase connection closed successfully")