from BaseModel import BaseModel

class BigramModel(BaseModel):
    def __init__(self, userActions=[], systemActions=[]):
        BaseModel.__init__(self, userActions, systemActions)

    def getUserActionCount(self, userAction, systemAction):
        if systemAction in self._actionsMap:
            if userAction in self._actionsMap[systemAction]:
                return self._actionsMap[systemAction][userAction]
            else:
                return 0
        else:
            return 0

    def getAllUserActionsCount(self, systemAction):
        return sum(self._actionsMap[systemAction].values())

    def getProbability(self, userAction, systemAction):
        return float(self.getUserActionCount(userAction, systemAction)) / float(self.getAllUserActionsCount(systemAction))
