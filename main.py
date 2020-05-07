from FilterMessage import FilterMessage
from webexteamssdk import WebexTeamsAPI
from databaseFunctions import dbFunctions
from WebExCalling import WebExActions

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

vaibhavT1 ={'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
 'created': '2020-05-07T02:27:31.742Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-05-07T02:29:35.349Z',
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTc3NzkyNTAtOTAwYS0xMWVhLWE4N2QtMDE4YzUzMzZmYTk2',
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

if __name__ == '__main__':
    action1 = WebExActions()
    dbObject = dbFunctions()
    filter1 = FilterMessage()
    print(filter1.get_object_id(tagged_message))