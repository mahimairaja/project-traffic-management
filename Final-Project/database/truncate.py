import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

tableName = input('Enter the table name to TRUNCATE : ')

query = f'''
delete from "{tableName}";
'''
cursor.execute(query)
conn.commit()

cursor.close()
conn.close()