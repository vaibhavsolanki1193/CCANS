
from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text, Number
from pyadaptivecards.components import TextBlock, Image, ImageSize
from pyadaptivecards.actions import Submit

class AdpCard():
    def __init__(self):
        self.Main_Banner = "https://i.imgur.com/uRFi2jX.png"
        self.Main_Banner_with_text = "https://i.imgur.com/AVR3OC6.png"

    def send_card(self, userObjId, inMsg, issueType, dbObj, webexObj):
        print("-->> AdaptiveCard.send_card():")
        # greeting = TextBlock("Critical Case Alert Notification",weight="bolder",horizontalAlignment="center")
        alert_type = TextBlock('Alert Type: PRI is Down',color="attention")
        req_action = TextBlock('\n\n Please collect the following: \n 1. show isdn status \n 2. show controller')
        CCANS_logo = Image(url=self.Main_Banner_with_text)
        submit = Submit(title="ACK",)
        card = AdaptiveCard(body=[CCANS_logo, alert_type, req_action], actions=[submit])
        attachment = {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": card.to_dict(),
                    }
        # roomId = inMsg['data']['roomId']
        webexObj.ccans_api.messages.create(toPersonId=userObjId, text="Card: Crtitical Case Alert", attachments=[attachment])
