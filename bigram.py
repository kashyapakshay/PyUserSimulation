class UserSimulation:
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

    def getProbability(self, userAction, systemAction):
        return float(self.getUserActionCount(userAction, systemAction)) / float(self.getAllUserActionsCount(systemAction))

    def getPredictedUserAction(self, systemAction):
        mostProbableUserAction = self._userActionsList[0]
        mostProbability = 0

        for userAction in self._userActionsList:
            userActionProbability = self.getProbability(userAction, systemAction)
            if userActionProbability > mostProbability:
                mostProbableUserAction = userAction
                mostProbability = userActionProbability

        return mostProbableUserAction

if __name__ == '__main__':
    # Test
    print '--- Testing ---\n'
    userSimulation = UserSimulation()

    print 'Recording \'fwd\' for \'fwd-inst\''
    userSimulation.recordAction('fwd', 'fwd-inst')
    print 'Recording \'back\' for \'fwd-inst\''
    userSimulation.recordAction('back', 'fwd-inst')
    print 'Recording \'left\' for \'fwd-inst\''
    userSimulation.recordAction('left', 'fwd-inst')
    print 'Recording \'left\' for \'fwd-inst\''
    userSimulation.recordAction('left', 'fwd-inst')
    print 'Recording \'right\' for \'fwd-inst\''
    userSimulation.recordAction('right', 'fwd-inst')

    print 'Recording \'fwd\' for \'back-inst\''
    userSimulation.recordAction('fwd', 'back-inst')
    print 'Recording \'back\' for \'back-inst\''
    userSimulation.recordAction('back', 'back-inst')

    print ''

    print 'User Actions List: ', userSimulation.getUserActions()
    print 'System Actions List: ', userSimulation.getSystemActions()

    print ''

    for systemAction in userSimulation.getSystemActions():
        for userAction in userSimulation.getUserActions():
            print 'Probability of \'%s\' for \'%s\': %f' % (userAction, systemAction, userSimulation.getProbability(userAction, systemAction))

    print ''

    print 'Predicted user action for \'fwd-inst\': ', userSimulation.getPredictedUserAction('fwd-inst')
    print 'Predicted user action for \'back-inst\': ', userSimulation.getPredictedUserAction('back-inst')
