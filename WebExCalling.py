from FilterMessage import FilterMessage
from webexteamssdk import WebexTeamsAPI
from xml.etree import ElementTree
from pprint import pprint
import re
from databaseFunctions import dbFunctions

""" Test message """

# delete them later
tagged_message = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
 'created': '2020-04-23T02:21:03.514Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-04-23T21:10:31.382Z',
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZGQ2NzQ3NjAtODVhNi0xMWVhLTgxMDUtMTUzYjg1Y2YyMzdk',
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

access_token = 'ZWE5NDI4NzEtYzZjOC00OTYyLWJmMjUtNDk4MWI5YmJmNjg0ZGIzOTBhZjktOWQ3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
ccans_api = WebexTeamsAPI(access_token=access_token)

class WebExActions():
    access_token = 'ZWE5NDI4NzEtYzZjOC00OTYyLWJmMjUtNDk4MWI5YmJmNjg0ZGIzOTBhZjktOWQ3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
    ccans_api = WebexTeamsAPI(access_token=access_token)

    def __init__(self):
        pass

    def get_extract_object_id(self, inmsg, dbObject):
        print("-->> WebexActions.get_extract_object_id():")
        """Finds the data-object-id and if it exist, it will check if the user
            exist in people table or not, and if not, it will write details in DB

        Args:
        inmsg(dict): incoming tagged
        dbObject: object to send commands to databaseFuntions.py  

        """
        message_text = inmsg['data']['text']
        pattern = "data-object-id=\"([^\"]+)\""
        # fetch object_ID from text saves it in a list
        ob_id = re.findall(pattern, message_text)
        # the second user_id object, first is for bot
        userId = ob_id[1]
        if dbObject.user_exist(userId) is False:
            userDet = self.ccans_api.people.get(userId)
            print("DB:Calling insert in people:")
            dbObject.insert_in_people(ob_id[1], userDet)
            print('user entry saved in table')
        else:
            print("send adaptive card")
            pass
        
    def Tagged_Message_Actions(self, inMsg, dbObject):
        extract_result = self.get_extract_object_id(inMsg, dbObject)


action1 = WebExActions()
dbObject = dbFunctions()
action1.get_extract_object_id(tagged_message, dbObject)

