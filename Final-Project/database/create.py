import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

table = '''
create table signal(
    Time date,
    lane_1 int,
    lane_2 int,
    lane_3 int,
    lane_4 int
)
'''

cursor.execute(table)
cursor.close()
print('Table created')