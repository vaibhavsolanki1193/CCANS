import sqlite3
from datetime import datetime


class dbFunctions():
    def __init__(self):
        self.con = sqlite3.connect(r"data/UCCANS_DB.sqlite")
        self.cur = self.con.cursor()

    def insert_in_tagged_table(self, issueType, inMsg):
        print("-->> databasefuntions.insert_in_tagged_table():")
        created = inMsg['data']['created']
        # strip last 5 unwanted digit and save as datetime object
        readableTime = datetime.strptime(created[:-5], '%Y-%m-%dT%H:%M:%S')
        msgId = inMsg['data']['id']
        markdown = inMsg['data']['markdown']
        email = inMsg['data']['personEmail']
        personId = inMsg['data']['personId']
        roomId = inMsg['data']['roomId']
        roomType = inMsg['data']['roomType']
        text = inMsg['data']['text']
        event = inMsg['event']
        taggedRow = (readableTime, msgId, markdown, email, personId, roomId, roomType, text, issueType, event)
        sql_insert = '''INSERT INTO TaggedMessage(created, messageId,markdown,
                        personEmail, personId, roomId, roomType, text, issueType, event)
                        VALUES (?,?,?,?,?,?,?,?,?,?)'''
        self.cur.execute(sql_insert, taggedRow)
        self.con.commit()

    def insert_in_people(self, objectId, peopleObject):
        print("-->> databaseFunctions.insert_in_people():")
        objId = objectId
        userId = peopleObject.id
        userName = peopleObject.displayName
        nickName = peopleObject.nickName
        lastName = peopleObject.lastName
        userMail = peopleObject.emails[0]
        peopleRow = (objId, userId, userName, nickName, lastName, userMail)
        sql_command = '''INSERT INTO People(objectId, id, DisplayName, nickName,lastName,
                            emailId) values (?,?,?,?,?,?)'''
        self.cur.execute(sql_command, peopleRow)
        self.con.commit()

    def show_table(self, tablename, name):
        print("-->> databasefunctions.show_table():")
        query = f"SELECT * from {tablename} WHERE nickName='{name}'"
        result = self.cur.rowcount
        print(result)
        print(type(result))
        print(result is -1)
        for row in self.cur.execute(query):
            print(row)

    def user_exist(self, objectId):
        print("""-->>databasefunctions.user_exist():""")
        query = (f"select id from People where objectId='{objectId}'")
        self.cur.execute(query)
        pointer = self.cur.fetchall()
        if len(pointer) == 0:
            print("User not found")
            return False
        else:
            print('user found')
            return True

    def insert_in_adaptive_card(self, inMsg, webexObj):
        print("""-->>databasefunctions.insert_in_adaptive_card():""")
        created = inMsg['data']['created']
        # strip last 5 unwanted digit and save as datetime object
        readableTime = datetime.strptime(created[:-5], '%Y-%m-%dT%H:%M:%S')
        msgId = inMsg['data']['id']
        personId = inMsg['data']['personId']
        roomId = inMsg['data']['roomId']
        roomType = inMsg['data']['roomType']
        text = inMsg['data']['text']
        event = inMsg['event']
        roomDetail = webexObj.ccans_api.rooms.get(roomId)
        roomTitle = roomDetail.title
        adaptiveCardRow = (readableTime, msgId, personId, roomId, roomType, roomTitle, text, event)
        sqlQuery = f"INSERT INTO AdaptiveCardAlert values (?,?,?,?,?,?,?,?)"
        self.cur.execute(sqlQuery, adaptiveCardRow)
        self.con.commit()

    def user_search_name(self, nickName):
        print("""-->>databasefunctions.insert_in_adaptive_card():""")
        sqlQuery = f"SELECT id from People where nickname='{nickName.capitalize()}'"
        self.cur.execute(sqlQuery)
        queryResult = self.cur.fetchall()
        if len(queryResult) == 0:
            return "NotFound"
        elif len(queryResult) == 1:
            return queryResult[0][0]
        else:
            return "NotFound"

    def insert_in_nonTagged_table(self, issueType, inMsg):
        print("-->> databasefuntions.insert_in_nontagged_table():")
        created = inMsg['data']['created']
        readableTime = datetime.strptime(created[:-5], '%Y-%m-%dT%H:%M:%S')
        msgId = inMsg['data']['id']
        markdown = inMsg['data']['markdown']
        email = inMsg['data']['personEmail']
        actorId = inMsg['data']['personId']
        roomId = inMsg['data']['roomId']
        roomType = inMsg['data']['roomType']
        text = inMsg['data']['text']
        event = inMsg['event']
        nonTaggedRow = (readableTime, msgId, markdown, email, actorId, roomId, roomType, text, issueType, event)
        sqlQuery = f"INSERT INTO NonTaggedMessage values (?,?,?,?,?,?,?,?,?,?)"
        self.cur.execute(sqlQuery, nonTaggedRow)
        self.con.commit()

    def __del__(self):
        self.con.close()


# internal testing
# dbObject = dbFunctions()
