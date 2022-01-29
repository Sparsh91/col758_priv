import numpy as np
import sys
"""
    A graph generator that takes two inputs n and p with p in [1/n , 1]
    It outputs m in the first line the number of edgese and then every line it will print 
    an edge u,v denoting u -> v
"""
def G(n,p):
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            has_an_edge = np.random.binomial(1,p)
            if(has_an_edge):
                edges.append((i,j))
    print(n)
    print(len(edges))
    for i in edges:
        print(i[0],i[1])

n = int(sys.argv[1])
p = float(sys.argv[2])
G(n,p)
