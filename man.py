from person import Person

class Man(Person):
    def __init__(self, id):
        super().__init__(id)
        self.proposedIndex = 0
    
    def getTopOption(self):
        return self.priorityList[self.proposedIndex]

    def reject(self):
        self.proposedIndex += 1
        self.setPartner(None)


    