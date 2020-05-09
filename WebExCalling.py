from webexteamssdk import WebexTeamsAPI


class WebExActions():
    access_token = 'ZWE5NDI4NzEtYzZjOC00OTYyLWJmMjUtNDk4MWI5YmJmNjg0ZGIzOTBhZjktOWQ3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
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
            adpCardObj.send_card(userObjId, inMsg, issueType, dbObj, webexObj)
        else:
            print("Calling send_adaptive_card(existing user)")
            adpCardObj.send_card(userObjId, inMsg, issueType, dbObj, webexObj)
