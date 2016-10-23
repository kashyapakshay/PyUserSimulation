import math
import random

import numpy as np
from sklearn import cluster

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

class BigramModel(UserSimulation):
    def __init__(self, userActions=[], systemActions=[]):
        UserSimulation.__init__(self, userActions, systemActions)

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

class ClusterModel(UserSimulation):
    def __init__(self, userActions=[], systemActions=[]):
        UserSimulation.__init__(self, userActions, systemActions)

        self.kMeansCluster = cluster.KMeans(n_clusters=2)
        self.clusterLabels = {}

    def updateClusters(self):
        data = []
        for userAction in self.getUserActions():
            for systemAction in self.getSystemActions():
                for i in range(0, self.getUserActionCount(userAction, systemAction)):
                    data.append([self._systemActionsList.index(systemAction), self._userActionsList.index(userAction)])

        data = np.array(data)

        # data = np.array([[systemAction, userAction] for i in range(0, self.getUserActionCount(userAction, systemAction)) for userAction in self.getUserActions() for systemAction in self.getSystemActions()])
        k = int(math.ceil(len(self.getSystemActions())/2.0))
        self.kMeansCluster = cluster.KMeans(n_clusters=k)

        self.kMeansCluster.fit(data)

        for pair in data.tolist():
            if pair[0] not in self.clusterLabels:
                self.clusterLabels[self._systemActionsList[pair[0]]] = self.kMeansCluster.labels_[data.tolist().index(pair)]

    def getClusters(self):
        return self.clusterLabels

    def recordAction(self, userAction, systemAction):
        UserSimulation.recordAction(self, userAction, systemAction)
        self.updateClusters()

    def getProbability(self, userAction, systemAction):
        cluster = self.clusterLabels[systemAction]

        clusterUserAction = 0
        clusterTotal = 0

        for systemAction2 in self.clusterLabels.keys():
            if self.clusterLabels[systemAction2] == cluster:
                clusterUserAction += self.getUserActionCount(userAction, systemAction2)
                clusterTotal += self.getAllUserActionsCount(systemAction2)

        return float(clusterUserAction) / float(clusterTotal)
