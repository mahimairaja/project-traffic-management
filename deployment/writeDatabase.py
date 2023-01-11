import json
import sqlite3
import threading
import time


conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

def writeToDatabase():
    while True :
        try :  
            with open("data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            jsonFile.close()
            x_value = time.strftime("%I:%M:%S", time.localtime())
            total_1 = data['lane_1']
            total_2 = data['lane_2']
            total_3 = data['lane_3']
            total_4 = data['lane_4']
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
        
if __name__ == "__main__":
    writeToDatabase()