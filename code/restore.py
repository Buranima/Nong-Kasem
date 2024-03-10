from maria import *
from config import *
from configW import *
import time

def restoreDB() :
    config()
    connectToDB()

    # dropSQL("DROP DATABASE !test")
    # time.sleep(1)
    # createSQL("CREATE DATABASE !test")

    dropSQL("DROP DATABASE nong_kasem")
    time.sleep(1)
    createSQL("CREATE DATABASE nong_kasem")

    time.sleep(1)
    connectToDB()
    createSQL("CREATE TABLE log_table(id_log INT(50) NOT NULL AUTO_INCREMENT, question_log VARCHAR(100) NOT NULL , PRIMARY KEY(id_log))")
    time.sleep(1)
    createSQL("CREATE TABLE answer_table(id_answer INT(50) NOT NULL AUTO_INCREMENT, answer VARCHAR(100) NOT NULL , PRIMARY KEY(id_answer))")
    time.sleep(1)
    createSQL("CREATE TABLE question_table(id_question INT(50) NOT NULL AUTO_INCREMENT, question VARCHAR(1000) NOT NULL COLLATE 'utf8mb4_general_ci', answer_fk INT(50) NOT NULL, PRIMARY KEY (id_question) USING BTREE, INDEX answer (answer_fk) USING BTREE, CONSTRAINT FK_question_table_answer_table FOREIGN KEY (answer_fk) REFERENCES answer_table (id_answer) ON UPDATE CASCADE ON DELETE CASCADE)")
    print("คืนค่าฐานข้อมูลเรียนร้อบ")

def restoreJson() :
    valueData = {
        "Name Robot": [
            {"nameBot": "น้องเกษม"}
        ],
        "Data Base": [
            {"dbUser": "root"},
            {"dbPassword": "1234"},
            {"dbHost": "127.0.0.1"},
            {"dbPort": 3306},
            {"dbName": "nong_kasem"}
        ],
        "Font": [
            {"font1": ("TH SarabunPSK", 48)},
            {"font2": ("TH SarabunPSK", 24)},
            {"font3": ("TH SarabunPSK", 18)}
        ]
    }
    setData(valueData)
    time.sleep(1)
    saveData()
    time.sleep(1)
    print("คืนค่าการตั้งค่าเรียบร้อย")

if __name__ == "__main__" :
    restoreJson()
    restoreDB()