import re


class FilterMessage():

    def __init__(self):
        pass

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
# res = fObj.main_filter(tagged_message)
# print(res)
