from pprint import pprint
import re

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

non_tagged_message = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
 'created': '2020-04-23T02:21:03.514Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-04-23T21:15:51.374Z',
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOWMyMjJlZTAtODVhNy0xMWVhLWIxNTUtMjVjZThlMjhjM2E3',
          'markdown': 'hookbusterBot1 non tagged space message',
          'personEmail': 'vasolank@cisco.com',
          'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
          'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMWM4ZWQzZDAtNzA2ZC0xMWVhLWJmOTgtOWRmOWU4NjY4ZmY0',
          'roomType': 'group',
          'text': '<p><spark-mention data-object-type="person" '
                  'data-object-id="e8c4e5eb-38f8-472c-a371-d886ba1f7798">hookbusterBot1</spark-mention> '
                  'non tagged space message</p>'},
 'event': 'created',
 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY',
 'ownedBy': 'creator',
 'resource': 'messages',
 'status': 'active'}

out_adaptive_card = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'created': '2020-04-23T02:21:03.514Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'attachments': [{'content': {'$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                                       'actions': [{'title': 'ACK',
                                                    'type': 'Action.Submit'}],
                                       'body': [{'text': 'CCANS- Critical Case '
                                                         'Alert Notification '
                                                         'System',
                                                 'type': 'TextBlock'},
                                                {'text': 'AlertType: PRI is '
                                                         'Down',
                                                 'type': 'TextBlock'},
                                                {'type': 'Image', 'url': '0'}],
                                       'type': 'AdaptiveCard',
                                       'version': '1.1'},
                           'contentType': 'application/vnd.microsoft.card.adaptive'}],
          'created': '2020-04-23T21:11:09.574Z',
          'files': ['https://api.ciscospark.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvZjQyYWVhNjAtODVhNi0xMWVhLTgxNjUtZWRmNGI1YmUxNjNlLzA'],
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZjQyYWVhNjAtODVhNi0xMWVhLTgxNjUtZWRmNGI1YmUxNjNl',
          'personEmail': 'hookbusterbot1@webex.bot',
          'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
          'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vM2ViZTA4ZjktOWZiZC0zYTIxLWE4YmQtOGMxZTExODgzYzJm',
          'roomType': 'direct',
          'text': 'Card: Crtitical Case Alert'},
 'event': 'created',
 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY',
 'ownedBy': 'creator',
 'resource': 'messages',
 'status': 'active'}

in_ack = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
 'created': '2020-04-23T02:21:03.514Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-04-23T21:11:22.340Z',
          'id': 'Y2lzY29zcGFyazovL3VzL0FUVEFDSE1FTlRfQUNUSU9OL2ZiYzZkYTQwLTg1YTYtMTFlYS05OTlkLTVkNzJmOWEzZDQ1Mw',
          'inputs': {},
          'messageId': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZjQyYWVhNjAtODVhNi0xMWVhLTgxNjUtZWRmNGI1YmUxNjNl',
          'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82YjQ4ZGZiYy0xYmU3LTRmYjEtOWM0NS1lMWRlODAzYjA1OWE',
          'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vM2ViZTA4ZjktOWZiZC0zYTIxLWE4YmQtOGMxZTExODgzYzJm',
          'type': 'submit'},
 'event': 'created',
 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY',
 'ownedBy': 'creator',
 'resource': 'attachmentActions',
 'status': 'active'}

unicast_message = {'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZmJlMGYxNi1lZGU3LTQ1NmYtOTUyOS04MTE3YTgyNWFhZTA',
 'created': '2020-05-07T02:27:31.742Z',
 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lOGM0ZTVlYi0zOGY4LTQ3MmMtYTM3MS1kODg2YmExZjc3OTg',
 'data': {'created': '2020-05-07T04:46:37.612Z',
          'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYmM1MTU2YzAtOTAxZC0xMWVhLTlmNjEtOTcwOTE1MDk3YTBm',
          'markdown': 'tes1',
          'personEmail': 'sancuriousvaibhav@gmail.com',
          'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZmJlMGYxNi1lZGU3LTQ1NmYtOTUyOS04MTE3YTgyNWFhZTA',
          'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vOGZmMWYzMjQtMzIxNC0zNzZlLTg4Y2EtNjEyZjU3Y2IxYmEz',
          'roomType': 'direct',
          'text': '<p>tes1</p>'},
 'event': 'created',
 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY',
 'ownedBy': 'creator',
 'resource': 'messages',
 'status': 'active'}
class FilterMessage():

    def __init__(self):
        pass

    def main_filter(self, unfitlered_message):
        try:
            if unfitlered_message['data'].get('markdown') and unfitlered_message['data']['text'].count('data-object-id') == 2:
                print('Tagged Message Received')
            elif unfitlered_message['data'].get('roomType') == 'direct':
                print('unicast message')
            elif unfitlered_message['data'].get('markdown') and unfitlered_message['data']['text'].count('data-object-id') is not 2:
                print("this in untagged message")
            elif unfitlered_message['data'].get('text') == 'Card: Crtitical Case Alert':
                print('Adaptive card detected')
            elif unfitlered_message['data'].get('type') == 'submit':
                print('Incoming ACK')
            else:
                print("No filtered matched")
        except Exception as e:
            print(e)

    def get_issue_type(self, inMsg):
        print("-->> FilterMessage.get_issue_type():")
        markdown = inMsg['data']['markdown']
        if 'pri' in markdown.lower():
            return "pri"
        elif 'gateway' in markdown.lower():
            return "gateway"

    def get_object_id(self, inMsg):
        print("-->> FilterMessage.get_object_id():")
        message_text = inMsg['data']['text']
        pattern = "data-object-id=\"([^\"]+)\""
        # fetch object_ID from text saves it in a list
        ob_id = re.findall(pattern, message_text)
        # the second user_id object, first is for bot
        userId = ob_id[1]
        return userId

# # internal testing 
# fObj = FilterMessage()
# fObj.main_filter(unicast_message)
