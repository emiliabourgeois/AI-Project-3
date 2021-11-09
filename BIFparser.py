import Node
from Graph import Graph
import numpy as np


def parseBIF(file):  # parses a BIF file, returning a graph of Nodes
    f = open(file)
    bif = f.readlines()

    lineCount = 0
    nodesList = []  # nodes are held in an array before being turned into a graph

    while lineCount < len(bif):
        lineList = bif[lineCount].split()

        if lineList[0] == 'variable':  # if the line is declaring a variable, creates a Node and appends it to the list
            name = lineList[1]
            lineCount += 1

            while bif[lineCount] != '}\n':
                lineList = bif[lineCount].split()

                if lineList[0] == 'type':
                    type = lineList[1]
                    num = int(lineList[3])
                    lineList[6:6 + num] = [x.strip(",") for x in lineList[6:6 + num]]  # removes commas from the states
                    states = lineList[6:6 + num]
                lineCount += 1

            nodesList.append(Node.Node(name, type, num, states))

        elif lineList[0] == 'probability':  # if the line is declaring probabilities for a variable, adds them to a
            # dictionary holding those conditional probabilities
            # adds spaces to parentheses so that they split correctly
            bif[lineCount] = bif[lineCount].replace('(', " ( ")
            bif[lineCount] = bif[lineCount].replace(')', " ) ")
            lineList = bif[lineCount].split()

            # finds which node we're working with
            for node in nodesList:
                if node.name == lineList[2]:
                    temp = node
                    break

            # if there is a connection between two nodes, adds them as parent and child
            if lineList[3] == '|':
                index = 4
                while lineList[index] != ')':
                    for node in nodesList:
                        if node.name == lineList[index].strip(","):
                            temp.addParent(node)
                            node.addChild(temp)
                    index += 1
            lineCount += 1

            # creates a dictionary that keeps track of the distributions for the
            stateDict = {}
            while bif[lineCount] != '}\n':
                lineList = bif[lineCount].split()

                # if marginal distributions are provided
                if lineList[0] == 'table':
                    del lineList[0]

                    # remove punctuation
                    for num in range(len(lineList)):
                        state = lineList[num]
                        state = state.replace('(', '')
                        state = state.replace(')', '')
                        state = state.replace(';', '')
                        state = state.replace(',', '')
                        lineList[num] = state

                    index = 0
                    for state in temp.states:
                        stateDict[state] = [float(lineList[index])]
                        index += 1

                # cleans the states from punctuation to make them easily insertable into the state field
                elif lineList[0][0] == "(":
                    for num in range(len(lineList)):
                        state = lineList[num]
                        state = state.replace('(', '')
                        state = state.replace(')', '')
                        state = state.replace(';', '')
                        state = state.replace(',', '')
                        lineList[num] = state

                    # creates keys based on the potential states of the node's parents.  example : TrueTrue formatted
                    # this way so states can be simply be added together to create the condition if there is > 1
                    index = 0
                    key = ""
                    for num in range(temp.numParents()):
                        key += lineList[index]
                        index += 1
                    value = lineList[temp.numParents():]
                    count = 0
                    for v in value:
                        value[count] = float(v)
                        count += 1
                    stateDict[key] = value

                lineCount += 1
            # sets the distribution of that node to the dictionary we made
            temp.setDistribution(stateDict)
        else:
            lineCount += 1

    # turns the resulting array into a graph, and topologically sorts it
    g = Graph(len(nodesList))
    for n in nodesList:
        for parent in n.parents:
            g.addEdge(parent, n)
        for child in n.children:
            g.addEdge(n, child)
    bn = np.array(g.topologicalSort(nodesList))
    newbn = bn[::-1]
    return newbn
