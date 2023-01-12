import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

query = '''
select * from signal;
'''

cursor.execute(query)
names = [description[0] for description in cursor.description]
data = cursor.fetchall()
print(names)
for row in data:
    print(row)

connection.close
cursor.close()