from person import Person

class Woman(Person):
    def __init__(self, id):
        super().__init__(id)

    def setPartner(self, partner):
        super().setPartner(partner)

    def setLine(self, line):
        self.line = line

    def getLine(self):
        return self.line

    def choosePreference(self, man1, man2):
        m1p = self.getPriority(man1)
        m2p = self.getPriority(man2)
        if m1p < m2p:
            return man1, man2
        else:
            return man2, man1
