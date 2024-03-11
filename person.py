from random import shuffle
class Person:
    def __init__(self, id):
        self.id = id
        self.partner = None
        self.point = None

    def setCirc(self, circ):
        self.circ = circ

    def getCirc(self):
        return self.circ

    def setPoint(self, point):
        self.point = point

    def getPoint(self):
        return self.point

    def getCoords(self):
        return self.point

    def setPartner(self, partner):
        self.partner = partner

    def getPriority(self, person):
        return self.priorityDict[person]

    def getPartner(self):
        return self.partner

    def randomlyPrioritize(self, options):
        self.priorityList = options.copy()
        shuffle(self.priorityList)

    def makePriorityDict(self):
        self.priorityDict = {}
        for i in range(len(self.priorityList)):
            self.priorityDict[self.priorityList[i]] = i
