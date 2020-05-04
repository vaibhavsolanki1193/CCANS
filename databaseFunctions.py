import sqlite3

teams_person = {
  "id": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE",
  "emails": [
    "vasolank@cisco.com"
  ],
  "phoneNumbers": [
    {
      "type": "work",
      "value": "+91 80 4429 9895"
    },
    {
      "type": "mobile",
      "value": "+91 783 885 7179"
    }
  ],
  "displayName": "Vaibhav Solanki",
  "nickName": "Vaibhav",
  "firstName": "Vaibhav",
  "lastName": "Solanki",
  "avatar": "https://8e325148c33e40909d40-0b990d1d119de8e505829619be483465.ssl.cf1.rackcdn.com/V1~6b48dfbc-1be7-4fb1-9c45-e1de803b059a~f5fdb04eb9f047509c58dbc3815012ee~1600",
  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY",
  "created": "2019-05-18T13:53:50.157Z",
  "status": "unknown",
  "type": "person"
}

class dbFunctions():
    def __init__(self):
        self.con = sqlite3.connect(r"data/UCCANS_DB.sqlite")
        self.cur = self.con.cursor()

    def insert_test(self, tup):
        sql_insert = """
                    INSERT INTO test(first, second) VALUES (?,?)"""

        self.cur.execute(sql_insert, tup)
        self.con.commit()

    def insert_in_tagged_table(self, taggedRow):
        print("-->> databasefuntions.insert_in_tagged_table():")
        sql_insert = '''INSERT INTO TaggedMessage(created, messageId,markdown,
                        personEmail, personId, roomId, roomType, text, event)
                        VALUES (?,?,?,?,?,?,?,?,?)'''
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

    def __del__(self):
        self.con.close()


# dbObject = dbFunctions()
# dbObject.show_table('People', 'Vikas')
# dbObject.insert_in_people(teams_person)
# print(dbObject.user_exist('Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YjRiNmVhNy0zZmY4LTQwZmUtYWY1Ny1iM2RmNWNmZDE5ZjY'))
# dbObject.user_exist('Y2lzY29zcGFyazovL3VzL1BFT1BMRS83YjRiNmVhNy0zZmY4LTQwZmUtYWY1Ny1iM2RmNWNmZDE5ZjY')