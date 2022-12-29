import csv
import random
import time
import sqlite3

x_value = 0 # Time data
total_1 = 0 # Lane 1 random data
total_2 = 0 # Lane 2 random data
total_3 = 0 # Lane 3 random data
total_4 = 0 # Lane 4 random data

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

# -- > Data generation into database 

try :
    while True :
        x_value = time.strftime("%I:%M:%S", time.localtime())
        total_1 = random.randint(15, 30)
        total_2 = random.randint(15, 30)
        total_3 = random.randint(15, 30)
        total_4 = random.randint(15, 30)
        query = f'''
        insert into signal
        values
        ("{x_value}", {total_1},{total_2},{total_3},{total_4});
        '''
        cursor.execute(query)
        conn.commit()
        print(x_value, total_1, total_2, total_3, total_3)
        time.sleep(10)
except KeyboardInterrupt:
    cursor.close()
    conn.close()
    print('Data Generator program ran successfully')
    
    
# -- > Same data generation with CSV

# attributes = ["Time", "lane_1", "lane_2", "lane_3", "lane_4"]

# # Writing the header file
# with open('data/data.csv', 'w') as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=attributes)
#     csv_writer.writeheader()

# try :
#     # Infinitely writing random data in csv
#     while True:
#         with open('data/data.csv', 'a') as csv_file:
#             csv_writer = csv.DictWriter(csv_file, fieldnames=attributes)
#             x_value = time.strftime("%I:%M:%S", time.localtime())
#             total_1 = random.randint(15, 30)
#             total_2 = random.randint(15, 30)
#             total_3 = random.randint(15, 30)
#             total_4 = random.randint(15, 30)
#             info = {
#                 "Time": x_value,
#                 "lane_1": total_1,
#                 "lane_2": total_2,
#                 "lane_3": total_3,
#                 "lane_4": total_4
#             }
#             print(x_value, total_1, total_2, total_3, total_3)
#             # Appending a row of data for every 10 seconds
#             csv_writer.writerow(info)
#         time.sleep(10)
        
# except KeyboardInterrupt :
#     print("Data Generator program ran successfully")