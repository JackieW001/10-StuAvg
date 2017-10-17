import sqlite3
import csv

db_name = "discobandit.db"
db = sqlite3.connect(db_name)
c = db.cursor()

get_stu_grades = "SELECT name, mark FROM peeps, courses WHERE peeps.id = courses.id"
table = c.execute(get_stu_grades)

names = {}
for i in table:
    if i[0] not in names:
        names[i[0]] = i[1]
    else:
        names[i[0]] += i[1]
print names


db.commit()
db.close()
