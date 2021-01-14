from webexteamssdk import WebexTeamsAPI


class WebExActions():
    access_token = 'YOUR BOT TOKEN'
    ccans_api = WebexTeamsAPI(access_token=access_token)

    def __init__(self):
        pass

    def tagged_Message_Actions(self, inMsg, dbObj, filterObj, adpCardObj, webexObj):
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
        dbObj.insert_in_tagged_table(issueType, inMsg)

        if dbObj.user_exist(userObjId) is False:
            userDet = self.ccans_api.people.get(userObjId)
            print("DB:Calling insert in people():")
            # save row in People table
            dbObj.insert_in_people(userObjId, userDet)
            print('user entry saved in table')
            print("Calling send_adaptive_card(new user)")
            adpCardObj.send_card(userObjId, issueType, dbObj, webexObj)
        else:
            print("Calling send_adaptive_card(existing user)")
            adpCardObj.send_card(userObjId, issueType, dbObj, webexObj)

    def non_tagged_message_action(self, inMsg, dbObj, filterObj, adpCardObj, webexObj):
        print("-->> WebExCalling.non_tagged_message_action():")
        if not inMsg['data'].get('markdown'):
            return False
        else:
            issueType = filterObj.get_issue_type(inMsg)
            messageText = inMsg['data']['markdown']
            print(messageText)
            possibleNickname = messageText.split('>')[-1].strip()
            searchName = dbObj.user_search_name(possibleNickname)
            dbObj.insert_in_nonTagged_table(issueType=issueType, inMsg=inMsg)
            print(searchName)
            if searchName == "NotFound":
                # send info to QM that alert failed
                roomId = inMsg['data']['roomId']
                failedMsg = inMsg['data']['markdown']
                failureMsg = f"""The message '{failedMsg}' appears to be in incorrect format and the CE has 'NOT' been notified of the case. Please fix the format. Tag bot and send message 'help' for more information. Think the format is correct ? Send the message screenshot to vasolank@cisco.com"""
                webexObj.ccans_api.messages.create(roomId=roomId, markdown=failureMsg)
            else:
                userId = searchName
                adpCardObj.send_card(userId, issueType=issueType, dbObj=dbObj, webexObj=webexObj)
                roomId = inMsg['data']['roomId']
                failedMsg = inMsg['data']['markdown']
                failureMsg = f"""The message '{failedMsg}' appears to be in incorrect format. CE is notified about the case however, please stick to the format and tag the CE. Tag bot and send message 'help' for more information. Think the format is correct ? Send the message screenshot to vasolank@cisco.com"""
                webexObj.ccans_api.messages.create(roomId=roomId, text=failureMsg)
