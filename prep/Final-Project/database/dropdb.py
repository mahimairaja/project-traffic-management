import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

tableName = input('Enter the table name to DROP : ')

query = f'''
drop table "{tableName}";
'''

cursor.execute(query)
cursor.close()