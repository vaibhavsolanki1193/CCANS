from databaseFunctions import dbFunctions
from WebExCalling import WebExActions
from adaptiveCard import AdpCard
from FilterMessage import FilterMessage


class MainThread():
    def __init__(self):
        pass

    def run_main_thread(self, messageType, inMsg):
        print("-->> MainThread.run_main_thread()")
        # creating objects
        webexObj = WebExActions()
        dbObj = dbFunctions()
        adpCardObj = AdpCard()
        filterObj = FilterMessage()
        if messageType == "TaggedMessage":
            webexObj.tagged_Message_Actions(inMsg, dbObj, filterObj, adpCardObj, webexObj)
        elif messageType == "AdaptiveCard":
            dbObj.insert_in_adaptive_card(inMsg=inMsg, webexObj=webexObj)
