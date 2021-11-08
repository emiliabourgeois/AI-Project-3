import math
import sys
import os
import Node
import numpy as np
import random
from fractions import Fraction

def enumerateAll(bn,variables,evidence):

def eliminationAsk(X,bn,evidence):
    for n in bn:
        for e in evidence:
            if e[0].casefold() == n.name.casefold():
                for c in n.states:
                    if e[1].casefold() == c.casefold():
                        n.state = e[1]
                        n.value = 1
    gone = []
    factors[s]
    varariables = []
    while len(gone) < len(bn):
        for n in bn:
            if n not in gone:
                variables.append[n]
    for v in variables:
        dist[keys[i]] = values[i]

    for var in variables()
        evidence.append(X)
        X.state = xi
        dist[xi] = enumerate_all(bn, variables, evidence)
