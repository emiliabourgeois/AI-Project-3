from collections import defaultdict

class Graph:
    def __init__(self, verts):
        self.V = verts
        self.g = defaultdict(list)

    def topSrt2(self, v, vs, s):
        vs.append(v)
        #append new v to visited
        for i in self.g[v]:
        # for all edges of vertex
            if i not in vs:
                # recursive call if not visited
                self.topSrt2(i, vs, s)
        s.append(v)

    def topSrt(self, bn):
        #visited vs
        vs = []
        #stack for sorting
        s = []
        #loop on each node then if not visited run topSrt2
        for i in bn:
            if i not in vs:
                self.topSrt2(i, vs, s)
        return s

    def e(self, u, v):
        #add an edge from parent to child
        self.g[u].append(v)