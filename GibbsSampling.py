import math
import sys
import os
import Node
import numpy as np
import random
from fractions import Fraction

def Normalize(a):
    s = float(sum(a))
    if s == 0:
        return [1/float(len(a)) for b in a]
    f = 1 / s
    return [f * p for p in a]

def prob(n):
    s = ""
    if len(n.parents) != 0:
        for p in n.parents:
            s += p.state
        x = n.distribution[s]
    else:
        s = n.state
        x = n.distribution[s]
    if(isinstance(x, (int, float))):
        return float(1)
    else:
        if len(x) > 1:
            Normalize(x)
            if 0.3333333 in x:
                return random.uniform(0.0,1.0)
            state = np.random.choice(n.states, p = x)
            vals = {}
            keys = n.states
            values = n.distribution[s]
            for i in range(len(keys)):
                vals[keys[i]] = values[i]
            if state.casefold() == n.state.casefold():
                return float(vals[state])
            else:
                return 1 - float(vals[state])
        else:
            return(float(x[0]))




def FillRandoms(Z):
    for i in Z:
        i.value = random.uniform(0.0, 1.0)
        i.updateState(i.value)


def Sample(i):
    D = [0 for j in range(len(i.states))]
    x = 0
    t = float(0)
    for val in i.states:
        i.state = val
        t = float(prob(i))
        for c in i.children:
            t *= float(prob(c))
        D[x] = t
        x+=1
    D = Normalize(D)
    return np.random.choice(i.states, p = D)

# X is query node, e is evidence, bn is the network, T is the amount of times Gibbs sampling will be repeated
def GB(X, bn, evidence):
    for n in bn:
        for e in evidence:
            if e[0].casefold() == n.name.casefold():
                for c in n.states:
                    if e[1].casefold() == c.casefold():
                        n.state = e[1]
                        #print(n.state)
                        n.value = 1
                        #print(n.name + " " + n.state)
    T = 1000
    decisions = 0
    N = [0 for k in range(len(X.states))] # counts for each value of X
    Z = [] # nonevidence variables
    count = 0
    for n in bn:
        if n.value != 1:
            Z.append(n)
    FillRandoms(Z)

    for j in range(T):
        for i in Z:
            i.state = Sample(i)
            decisions += 1
            count = 0
            for s in X.states:
                if X.state.casefold() == s.casefold():
                    N[count] += 1
                count += 1
            count = 0
    decisions += 1
    return Normalize(N), decisions, evidence