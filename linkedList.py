from node import Node
class LinkedList:
    def __init__(self, list):
        self.start = None
        self.end = None
        self.makeList(list)

    def isEmpty(self):
        if self.start == None:
            return True
        else:
            return False

    def makeList(self, list):
        g = None
        prior = None
        count = 0
        for obj in list:
            node = Node()
            node.setContent(obj)
            node.setPrior(prior)
            if node.getPrior() != None:
                node.getPrior().setNext(node)
            prior = node
            if count == 0:
                self.start = node
            count +=1
            g = node
        self.end = g

    def show(self):
        node = self.start
        count = 0
        while node != self.end:
            node = node.getNext()
            count += 1
            print(count)

    def add(self, obj):
        #adds node to end of linked list
        node = Node()
        node.setContent(obj)
        node.setPrior(self.end) 
        node.getPrior().setNext(node)
        self.end = node
        if self.start == None:
            self.start = node 

    def remove(self):
        self.start = self.start.getNext()

    def pullOneElement(self):
        out = self.start.getContent()
        self.remove()
        return out
        