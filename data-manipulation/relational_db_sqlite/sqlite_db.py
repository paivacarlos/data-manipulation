import sqlite3
import os
os.remove("utils_db/school.db") if os.path.exists("utils_db/school.db") else None

#creating a connection with database
#if database dont exist it will be create
con = sqlite3.connect('utils_db/school.db')
print(type(con))

#create a cursor
cur = con.cursor()
print(type(cur))

#instruction to create a db
sql_create = 'create table courses' \
             '(id integer primary key ,' \
             'title varchar(100), ' \
             'category varchar(100))'

#executing the sql instruction in the cursor
cur.execute(sql_create)

#instruction insert
sql_insert = 'insert into courses values (?, ? ,?)'

#dada
recset = [(1000, 'Ciência de dados', 'Data Scince'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

#inserting data registers
for rec in recset:
    cur.execute(sql_insert, rec)

#reccording data
con.commit()

#sql instruction select
sql_select = 'select * from courses'

#select all register in the db
cur.execute(sql_select)
data = cur.fetchall()

#show the data
for line in data:
    print('Course: %d, Title: %s, Category: %s \n' % line)

#inserting more registers
recset = [(1003, 'Gestão de dados com o Mongo', 'Big Data'),
          (1004, 'R Fundamentos', 'Análises de Dados')]

for rec in recset:
    cur.execute(sql_insert, rec)

con.commit()

#instructions directly
cur.execute('select * from courses')
recset = cur.fetchall()
for rec in recset:
    print('Curso ID: %d, Title: %s, Category: %s' % rec)

con.close()