class Node:

    def __init__(self, name, type, num, states):
        self.name = name
        self.type = type
        self.num = num
        self.states = states
        self.children = []
        self.parents = []
        self.distribution = None
        self.marginal = None
        self.value = None

    def addChild(self, child):
        self.children.append(child)

    def numParents(self):
        return len(self.parents)

    def isRoot(self):
        return self.numParents() == 0

    def addParent(self, parent):
        self.parents.append(parent)

    def setDistribution(self, dist):
        self.distribution = dist
        if self.isRoot():
            self.marginal = dist

    def getMarkovBlanket(self):
        blanket = []
        blanket += self.children
        blanket += self.parents
        for child in self.children:
            blanket += child.parents
        blanket = removeDupes(blanket)
        return blanket


def removeDupes(array):
    runningList = []
    for i in array:
        if i not in runningList:
            runningList.append(i)
    return runningList
