import random

class BaseModel:
    def __init__(self, userActions=[], systemActions=[]):
        self._userActionsList = []
        self._systemActionsList = []

        self._actionsMap = {}

        for systemAction in systemActions:
            self._actionsMap[systemAction] = {}
            for userAction in userActions:
                self._actionsMap[systemAction][userAction] = 0

    def addNewUserAction(self, newUserAction):
        if newUserAction not in self._userActionsList:
            self._userActionsList.append(newUserAction)

    def getUserActions(self):
        return self._userActionsList

    def addNewSystemAction(self, newSystemAction):
        if newSystemAction not in self._systemActionsList:
            self._systemActionsList.append(newSystemAction)

    def getSystemActions(self):
        return self._systemActionsList

    def updateActionsMap(self, userAction, systemAction):
        if systemAction not in self._actionsMap:
            self._actionsMap[systemAction] = {}

        if userAction not in self._actionsMap[systemAction]:
            self._actionsMap[systemAction][userAction] = 0

        self._actionsMap[systemAction][userAction] += 1

    def recordAction(self, userAction, systemAction):
        self.addNewUserAction(userAction)
        self.addNewSystemAction(systemAction)
        self.updateActionsMap(userAction, systemAction)

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

    def getPredictedUserAction(self, systemAction):
        mostProbableUserAction = self._userActionsList[0]
        mostProbability = 0

        for userAction in self._userActionsList:
            userActionProbability = self.getProbability(userAction, systemAction)
            if userActionProbability > mostProbability:
                mostProbableUserAction = userAction
                mostProbability = userActionProbability
            elif userActionProbability == mostProbability:
                # Randomly either switch or stick with current mostProbableUserAction when there
                # are equally likely actions
                # Lower flip chance for exploration
                flip = random.randint(1, 10)
                flipChance = 5
                if flip > flipChance:
                    mostProbableUserAction = userAction

        return mostProbableUserAction
