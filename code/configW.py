import json

file_Name = 'config.json'
data = None

def setData(dataSet) :
    global data
    data = dataSet

def saveData() :
    global file_Name, data
    with open(file_Name, 'w') as file:
        json.dump(data, file, indent=3)

def changeData(category = None, dataKeyWord = None, dataValue = None) :
    global data
    for index, item in enumerate(data[category]):
        if dataKeyWord in item:
            data[category][index][dataKeyWord] = dataValue
            break
    else:
        print("ไม่พบข้อมูลที่ต้องการเปลี่ยน")

if __name__ == "__main__" :
    data = {
        "Name Robot": [
            {"nameBot": "น้องเกษม"}
        ],
        "Data Base": [
            {"dbUser": "root"},
            {"dbPassword": "1234"},
            {"dbHost": "127.0.0.1"},
            {"dbPort": 3306},
            {"dbName": "nong_kasem"},
        ]
    }
    setData(data)
    # changeData("Name Robot", "nameBot", "น้องเกษม")
    saveData()