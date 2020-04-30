from FilterMessage import FilterMessage
from webexteamssdk import WebexTeamsAPI
from xml.etree import ElementTree
from pprint import pprint
import re

""" Test message """ # delete them later 
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


class WebExActions():
    access_token = 'ZWE5NDI4NzEtYzZjOC00OTYyLWJmMjUtNDk4MWI5YmJmNjg0ZGIzOTBhZjktOWQ3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
    ccans_api = WebexTeamsAPI(access_token=access_token)
    
    def __init__(self):
        pass

    def get_extract_object_id(self, inmsg):
        """Finds the data-object-id

        Args:
        inmsg(dict): incoming tagged message 

        """
        message_text = inmsg['data']['text']
        pattern = "data-object-id=\"([^\"]+)\""
        ob_id = re.findall(pattern,message_text)        # fetch object_ID from text 
        print(ob_id)                                    # saves it in a list 
        user_id = ob_id[1]                              # the second user_id object, first is for bot 
        user_det = self.ccans_api.people.get(user_id)
        user_mail = user_det.emails[0]
        user_name = user_det.displayName
        



action1 = WebExActions()
action1.get_extract_object_id(tagged_message)



