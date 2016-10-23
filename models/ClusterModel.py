import math
import numpy as np
from sklearn import cluster

from BaseModel import BaseModel

class ClusterModel(BaseModel):
    def __init__(self, userActions=[], systemActions=[]):
        BaseModel.__init__(self, userActions, systemActions)

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
        BaseModel.recordAction(self, userAction, systemAction)
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
