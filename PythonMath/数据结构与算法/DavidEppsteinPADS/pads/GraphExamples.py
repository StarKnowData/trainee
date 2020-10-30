"""GraphExamples.py

Various examples of small standard named graphs.

D. Eppstein, September 2005.
"""

def GeneralizedPetersenGraph(n,k):
    G = {}
    for i in range(n):
        G[i,True] = (i,False),((i-1)%n,True),((i+1)%n,True)
        G[i,False] = (i,True),((i-k)%n,False),((i+k)%n,False)
    return G

PetersenGraph = GeneralizedPetersenGraph(5,2)
DesarguesGraph = GeneralizedPetersenGraph(10,3)

def GeneralizedCoxeterGraph(n,a,b):
    G = {}
    for i in range(n):
        G[i,0] = (i,1),(i,2),(i,3)
        G[i,1] = (i,0),((i+1)%n,1),((i-1)%n,1)
        G[i,2] = (i,0),((i+a)%n,2),((i-a)%n,2)
        G[i,3] = (i,0),((i+b)%n,1),((i-b)%n,1)
    return G

CoxeterGraph = GeneralizedCoxeterGraph(7,2,3)

def CubeConnectedCycles(n):
    return {(x,y):[(x,(y+1)%n),(x,(y-1)%n),(x^(1<<y),y)]
            for x in range(1<<n) for y in range(n)}

def LCFNotation(L,n):
    """
    Construct the cubic Hamiltonian graph with LCF Notation L^n.
    See http://mathworld.wolfram.com/LCFNotation.html
    for a description of this notation.
    """
    n *= len(L)
    return {i:((i-1)%n,(i+1)%n,(i+L[i%len(L)])%n) for i in range(n)}

McGeeGraph = LCFNotation([-12,7,-7],8)
DyckGraph = LCFNotation([-13,5,-5,13],8)
PappusGraph = LCFNotation([5,7,-7,7,-7,-5],3)
TutteCoxeterGraph = LCFNotation([-13,-9,7,-7,9,13],5)
GrayGraph = LCFNotation([-25,7,-7,13,-13,25],9)
