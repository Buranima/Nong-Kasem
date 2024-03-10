import json

nameBot = None

dbUser = None
dbPassword = None
dbHost = None
dbPort = None
dbName = None

font1 = None
font2 = None
font3 = None

def config() :
    global nameBot, dbUser, dbPassword, dbHost, dbPort, dbName, font1, font2, font3
    with open('config.json', 'r') as json_file:
        data = json.load(json_file)
        
    nameBot = data["Name Robot"][0]["nameBot"]
    dbUser = data["Data Base"][0]["dbUser"]
    dbPassword = data["Data Base"][1]["dbPassword"]
    dbHost = data["Data Base"][2]["dbHost"]
    dbPort = data["Data Base"][3]["dbPort"]
    dbName = data["Data Base"][4]["dbName"]
    font1 = tuple(data["Font"][0]["font1"])
    font2 = tuple(data["Font"][1]["font2"])
    font3 = tuple(data["Font"][2]["font3"])

config()

if __name__ == "__main__" :
    print(nameBot)
    print(dbUser)
    print(dbPassword)
    print(dbHost)
    print(dbPort)
    print(dbName)
    print(font1)
    print(font2)
    print(font3)