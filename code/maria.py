import mariadb
from config import *

cursor = None
connectDB = None

def connectToDB() :
    global cursor, connectDB
    try:
        connectDB = mariadb.connect(
            user = dbUser,
            password = dbPassword,
            host = dbHost,
            port = dbPort,
            database = dbName
            )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
    cursor = connectDB.cursor()

def browseSQL(sqlCommand) :
    global cursor
    answerList = []
    cursor.execute(sqlCommand)
    result = cursor.fetchall()
    #print(result)
    for data in result :
        dataString = str(data)
        dataString = dataString.replace("'", "")
        dataString = dataString.replace(",", "")
        dataString = dataString.replace("(", "")
        dataString = dataString.replace(")", "")
        answerList.append(dataString)
    #print(len(answerList))
    return answerList

def increaseSQL(sqlCommand) :
    global cursor, connectDB
    cursor.execute(sqlCommand)
    connectDB.commit()

def dropSQL(sqlCommand) :
    global cursor, connectDB
    cursor.execute(sqlCommand)
    connectDB.commit()

def createSQL(sqlCommand) :
    global cursor, connectDB
    cursor.execute(sqlCommand)
    connectDB.commit()

def deleteSQL(sqlCommand) :
    global cursor, connectDB
    cursor.execute(sqlCommand)
    connectDB.commit()

if __name__ == "__main__" :
    connectToDB()
    # result = browseSQL("SELECT question FROM question_table")
    # print(result)
    # increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str("555") + "', " + str(4) + ")")
    #dropSQL("DROP TABLE log_table")
    #createSQL("CREATE TABLE log_table(id_log INT(50) NOT NULL AUTO_INCREMENT, question_log VARCHAR(100) NOT NULL , PRIMARY KEY(id_log))")
    #deleteSQL("DELETE FROM log_table WHERE  id_log = 2")