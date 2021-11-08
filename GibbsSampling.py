import math
import sys
import os

def FillRandoms(x, Z):
    e = x
    for i in x:
        if x[i] not in e:
            x[i] = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
    return x

def Sample():
    ## aalogic
    return

def GibbsSampling(X, e, bn, T):
    decisions = 0
    x = e #current state of network
    N = [] # vector of counts for each value of X
    Z = [] #nonevidence variables
    genZ()
    x = fillrandoms(x,Z)
    for j in range(1, T+1):
        for i in Z:
            x[i] = Sample(i,i.markovBlanket())
            decisions += 1
            N[math.floor(float(X)*X.vars)] += 1
    decisions += 1
    return Normalize(N), desicions