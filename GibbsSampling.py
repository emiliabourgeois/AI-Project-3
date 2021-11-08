import math
import sys
import os
import Node
import numpy as np

def prob(n):
    s = ""
    if len(n.parents) != 0:
        for p in parents:
            s += p.state
        x = n.distribution[s]
    else:
        return n.distribution[n.state]
    if(isinstance(x, (int, float))):
        return x
    return np.random.choice(x, p = x)

def Normalize(a):
    f = 1 / sum(a)
    return [f * p for p in a]


def FillRandoms(Z):
    for i in Z:
        i.value = random.uniform(0.0, 1.0)
        i.updateState(i.value)
    return x


def Sample(i, mb):
    D = [0 for j in range(len(X.vars))]
    c = 0
    t = float(0)
    for val in i.getvars:
        t = float(prob(i))
        c = 0
        for c in i.children:
            t *= prob(c)
        c += 1
    D = Normalize(D)
    np.random.choice(i.getvars, p = D)
    return

# X is query node, e is evidence, bn is the network, T is the amount of times Gibbs sampling will be repeated
def GibbsSampling(X, e, bn):
    T = 1000
    decisions = 0
    N = [0 for k in range(X.vars)] # counts for each value of X
    Z = [] # nonevidence variables
    for n in bn:
        if n.value == 0:
            Z.append(n)
    FillRandoms(Z)
    for j in range(1, T):
        for i in Z:
            i.state = Sample(i, i.markovBlanket())
            i.updateState(i.value)
            decisions += 1
            N[int(float(X.value)*X.vars)] += 1
    decisions += 1
    return Normalize(N), desicions, X