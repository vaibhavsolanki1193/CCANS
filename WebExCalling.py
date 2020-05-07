from FilterMessage import FilterMessage
from webexteamssdk import WebexTeamsAPI
from databaseFunctions import dbFunctions
from adaptiveCard import AdpCard

""" Test message """

# delete them later
tagged_message = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
 'created': '2020-04-23T02:21:03.514Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-04-23T21:10:31.382Z',
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZGQ2NzQ3NjAtODVhNi0xMWVhLTgxMDUtMTUzYjg1Y2YyMzd1',
          'markdown': 'hookbusterBot1 tid3 > PRI > Vikas',
          'personEmail': 'vasolank@cisco.com',
          'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
          'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMWM4ZWQzZDAtNzA2ZC0xMWVhLWJmOTgtOWRmOWU4NjY4ZmY0',
          'roomType': 'group',
          'text': '<p><spark-mention data-object-type="person" '
                  'data-object-id="e8c4e5eb-38f8-472c-a371-d886ba1f7798">hookbusterBot1</spark-mention> '
                  'tid3 &gt; PRI &gt; <spark-mention data-object-type="person" '
                  'data-object-id="7b4b6ea7-3ff8-40fe-af57-b3df5cfd19f6">Vikas</spark-mention></p>'},
 'event': 'created',
 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY',
 'ownedBy': 'creator',
 'resource': 'messages',
 'status': 'active'}

vaibhavT1 = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
 'created': '2020-05-07T02:27:31.742Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-05-07T02:29:35.349Z',
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTc3NzkyNTAtOTAwYS0xMWVh1WE4N2Qt1DE4Yz1zMzZ1YT12',
          'markdown': 'hookbusterBot1 tid6 > PRI > Vaibhav Solanki T1',
          'personEmail': 'vasolank@cisco.com',
          'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
          'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMWM4ZWQzZDAtNzA2ZC0xMWVhLWJmOTgtOWRmOWU4NjY4ZmY0',
          'roomType': 'group',
          'text': '<p><spark-mention data-object-type="person" '
                  'data-object-id="e8c4e5eb-38f8-472c-a371-d886ba1f7798">hookbusterBot1</spark-mention> '
                  'tid6 &gt; PRI &gt; <spark-mention data-object-type="person" '
                  'data-object-id="6fbe0f16-ede7-456f-9529-8117a825aae0">Vaibhav '
                  'Solanki T1</spark-mention></p>'},
 'event': 'created',
 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY',
 'ownedBy': 'creator',
 'resource': 'messages',
 'status': 'active'}

class WebExActions():
    access_token = 'ZWE5NDI4NzEtYzZjOC00OTYyLWJmMjUtNDk4MWI5YmJmNjg0ZGIzOTBhZjktOWQ3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
    ccans_api = WebexTeamsAPI(access_token=access_token)

    def __init__(self):
        pass


    def tagged_Message_Actions(self, inMsg, dbObject, filterObject, adpCardObj, webexObj):
        print("-->> WebExCalling.tagged_Message_Actions():")
        """Finds the data-object-id and if it exist, it will check if the user
            exist in people table or not, and if not, it will write details in DB

        Args:
        inmsg(dict): incoming tagged
        dbObject: object to send commands to databaseFuntions.py  

        """
        userObjId = filterObj.get_object_id(inMsg)
        # filter markdown text to find type of issue
        issueType = filterObj.get_issue_type(inMsg)
        # save row in taggedMessage table
        dbObj.insert_in_tagged_table(inMsg)

        if dbObj.user_exist(userObjId) is False:
            userDet = self.ccans_api.people.get(userObjId)
            print("DB:Calling insert in people():")
            # save row in People table
            dbObj.insert_in_people(userObjId, userDet)
            print('user entry saved in table')
            print("Calling send_adaptive_card(old user)")
            adpCardObj.send_card(userObjId, inMsg, issueType, dbObj, webexObj)
        else:
            print("Calling send_adaptive_card(new user)")
            adpCardObj.send_card(userObjId, inMsg, issueType, dbObj, webexObj)


#main function 
webexObj = WebExActions()
dbObj = dbFunctions()
filterObj = FilterMessage()
adpCardObj = AdpCard()
webexObj.tagged_Message_Actions(vaibhavT1, dbObj, filterObj, adpCardObj, webexObj)



