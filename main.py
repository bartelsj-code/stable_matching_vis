
from time import sleep
from graphics import *
from linkedList import LinkedList
from node import Node
from man import Man
from woman import Woman
import math


class Pairer:
    def __init__(self, quant, drawing):
        self.quant = quant

        self.colorFactor = 300
        self.drawing = drawing
        self.width = 1500
        self.border = 1200/quant
        self.distance = self.width - 2*self.border
        self.spacer = self.distance/(quant - 1)
        self.win = GraphWin("Stable Matching", self.width, 500)
        self.win.setBackground(color_rgb(30,30,30))
        self.men, self.women, self.all = makeIndividuals(quant, self.spacer, self.border)
        if self.drawing:
            self.drawIndividuals()
        self.freeMen = LinkedList(self.men)

    def drawIndividuals(self):
        for individual in self.all:
            rad = 600/self.quant
            if rad < 4:
                rad = 4
            if rad > 50:
                rad = 50
            circ = Circle(individual.getPoint(), rad)
            individual.setCirc(circ)
            circ.setFill("white")
            circ.setWidth(1)
            circ.draw(self.win)

    def pair(self):
        sleep(5/self.quant)
        count = 0
        while not self.freeMen.isEmpty() and count < self.quant ** 2:
            man = self.freeMen.pullOneElement()
            man.getCirc().setWidth(4)
            woman = man.getTopOption()
            woman.getCirc().setWidth(4)
            if woman.getPartner() == None:
                # print("easy")
                woman.setPartner(man)
                man.setPartner(woman)
                if self.drawing:
                    line = Line(woman.getPoint(), man.getPoint())
                    line.setOutline(color_rgb(130,130,130))
                    woman.setLine(line)
                    line.draw(self.win)
                    f = math.floor(255*(woman.getPriority(man)/self.quant))
                    woman.getCirc().setFill(color_rgb(f, 255-f, 0))
                    man.getCirc().setFill(color_rgb(0,255,0))
            else:
                # print("trouble")
                man2 = woman.getPartner()
                chosenMan, rejectedMan = woman.choosePreference(man, man2)
                woman.setPartner(chosenMan)
                chosenMan.setPartner(woman)
                if self.drawing:
                    woman.getLine().undraw()
                    line = Line(woman.getPoint(), chosenMan.getPoint())
                    line.setOutline(color_rgb(130,130,130))
                    line.draw(self.win)
                    woman.setLine(line)
                    f = math.floor(255*(woman.getPriority(chosenMan)/self.quant))
                    woman.getCirc().setFill(color_rgb(f, 255-f, 0))
                    rejectedMan.getCirc().setFill(color_rgb(255,255,255))
                    m = math.floor(255 * (chosenMan.getPriority(chosenMan.getPartner())/self.quant))
                    chosenMan.getCirc().setFill(color_rgb(m,  255-m  ,0))
                self.freeMen.add(rejectedMan)
                rejectedMan.reject()
            sleep(5/self.quant)
            man.getCirc().setWidth(1)
            woman.getCirc().setWidth(1)
    
def makeIndividuals(quantity, spacer, border):
    women = []
    men = []
    all = []
    for i in range(quantity):
        x = i * spacer + border
        y = 250
        woman = Woman(i)
        man = Man(i)
        woman.setPoint(Point(x, y + 150))
        man.setPoint(Point(x, y - 150))
        women.append(woman)
        men.append(man)
        all.append(woman)
        all.append(man)
    for woman in women:
        woman.randomlyPrioritize(men)
        
        woman.makePriorityDict()
    for man in men:
        man.randomlyPrioritize(women)
        man.makePriorityDict()
    return men, women, all




if __name__ == "__main__":
    count = int(input("number of individuals on each side: "))
    pairer = Pairer(count, True)
    pairer.pair()
    manH = 0
    womH = 0
    matched = True
    for man in pairer.men:
        if man.getPartner().getPartner() != man:
            matched = False
        
        manH += man.getPriority(man.getPartner())
        womH += man.getPartner().getPriority(man)
    manAH = manH/count
    womAH = womH/count
    print("Matched: {}".format(matched))
    print("Man Average Happiness: {}    Woman Average Happiness: {}".format(manAH, womAH))
    g = input("g")
