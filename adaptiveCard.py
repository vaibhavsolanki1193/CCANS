from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.components import TextBlock, Image
from pyadaptivecards.actions import Submit


class AdpCard():
    def __init__(self):
        self.Main_Banner = "https://i.imgur.com/uRFi2jX.png"
        self.Main_Banner_with_text = "https://i.imgur.com/AVR3OC6.png"

    def send_card(self, userObjId, issueType, dbObj, webexObj):
        print("-->> AdaptiveCard.send_card():")
        IssueActionMapping = {
            'pri': '\n\n These details might help:\n 1. show isdn status \n 2. show controller',
            'gateway': '\n\n These details might help: \n 1. show ccm-manager\n 2. show isdn status \n 3. Check for crash files\n 4. Check for uptime'
        }
        AlertTextMapping = {
            'pri': 'PRI is Down',
            'gateway': 'Gateway is unreachable'
        }
        # greeting = TextBlock("Critical Case Alert Notification",weight="bolder",horizontalAlignment="center")
        alertType = TextBlock(f'Alert Type:{AlertTextMapping[issueType]}', color="attention")
        reqAction = TextBlock(f'{IssueActionMapping[issueType]}')
        CCANSLogo = Image(url=self.Main_Banner_with_text)
        submit = Submit(title="ACK",)
        card = AdaptiveCard(body=[CCANSLogo, alertType, reqAction], actions=[submit])
        attachment = {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": card.to_dict(),
                    }
        # roomId = inMsg['data']['roomId']
        webexObj.ccans_api.messages.create(toPersonId=userObjId, text="Card: Crtitical Case Alert", attachments=[attachment])
