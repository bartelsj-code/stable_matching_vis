class Node:
    def __init__(self):
        self.content = None
        self.prior = None
        self.next = None
        
    def setPrior(self, prior):
        self.prior = prior

    def getPrior(self):
        return self.prior

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content