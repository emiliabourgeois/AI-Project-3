from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):

        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.append(v)

    def topologicalSort(self, bn):

        visited = []
        stack = []
        for i in bn:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        return stack