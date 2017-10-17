import sqlite3
import csv

db_name = "discobandit.db"
db = sqlite3.connect(db_name)
c = db.cursor()

c.execute("CREATE TABLE peeps_avg (name TEXT, id INTEGER, avg INTEGER);")

names = c.execute("SELECT name from peeps;")

# put names in list
name_list = []
for name in names:
    name_list.append(name[0])

for name in name_list:
    
    # calculate averages
    g_sum = 0
    courses = 0
    grades = c.execute("SELECT mark FROM courses,peeps where peeps.id = courses.id and peeps.name='%s';" % name)
    for grade in grades:
        g_sum += grade[0]
        courses +=1
    avg = g_sum/courses
    print name
    print avg

    # getting student id
    stu_id = c.execute("SELECT id FROM peeps WHERE name = '%s';"%name)
    for i in stu_id:
        stu_id = i
    stu_id = stu_id[0]

    # inserting into peeps_avg
    command = "INSERT INTO peeps_avg VALUES ('%s',%s,%s);"%(name,stu_id,avg)
    print command
    c.execute(command)
    
db.commit()
db.close()
