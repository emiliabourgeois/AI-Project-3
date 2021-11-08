import Node
import re


def parseBIF(file):
    f = open(file)
    bif = f.readlines()

    lineCount = 0
    nodesList = []

    while lineCount < len(bif):
        lineList = bif[lineCount].split()

        if lineList[0] == 'variable':
            name = lineList[1]
            lineCount += 1

            while bif[lineCount] != '}\n':
                lineList = bif[lineCount].split()

                if lineList[0] == 'type':
                    type = lineList[1]
                    num = int(lineList[3])
                    lineList[6:6 + num] = [x.strip(",") for x in lineList[6:6 + num]]
                    states = lineList[6:6 + num]
                lineCount += 1

            nodesList.append(Node.Node(name, type, num, states))

        elif lineList[0] == 'probability':
            bif[lineCount] = bif[lineCount].replace('(', " ( ")
            bif[lineCount] = bif[lineCount].replace(')', " ) ")
            lineList = bif[lineCount].split()

            for node in nodesList:
                if node.name == lineList[2]:
                    temp = node
                    break

            if lineList[3] == '|':
                index = 4
                while lineList[index] != ')':
                    for node in nodesList:
                        if node.name == lineList[index].strip(","):
                            temp.addParent(node)
                            node.addChild(temp)
                    index += 1
            lineCount += 1

            stateDict = {}
            # While the end of the declaration is not parsed
            while bif[lineCount] != '}\n':
                lineList = bif[lineCount].split()

                if lineList[0] == 'table':
                    # Get rid of the identifier
                    del lineList[0]

                    # Get rid of commas and semicolons
                    for num in range (len(lineList)):
                        state = lineList[num]
                        state = state.replace('(', '')
                        state = state.replace(')', '')
                        state = state.replace(';', '')
                        state = state.replace(',', '')
                        lineList[num] = state

                    # Store the distribution (this is a marginal distribution)
                    index = 0
                    for state in temp.states:
                        stateDict[state] = [float(lineList[index])]
                        index += 1

                elif lineList[0][0] == "(":
                    # Remove all punctuation from the evidence names and the probability values
                    for num in range (len(lineList)):
                        state = lineList[num]
                        state = state.replace('(', '')
                        state = state.replace(')', '')
                        state = state.replace(';', '')
                        state = state.replace(',', '')
                        lineList[num] = state

                    # In the CPD dictionary key, the states of the node are stored first. The second tuple is that of the parent values
                    index = 0
                    key = ""
                    for num in range(temp.numParents()):
                        key += lineList[index]
                        index += 1
                    value = lineList[temp.numParents():]
                    stateDict[key] = value

                lineCount += 1
            # print stateDict
            temp.setDistribution(stateDict)
        else:
            lineCount += 1
    return nodesList
