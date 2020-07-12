#from karma.graph import *
from karma.graph import NewGraph,addVertex,getVertices,getEdges

if __name__ == '__main__':
    # a ->  b,d
    # b ->  c,a
    # c ->  d,b
    # d ->  a,c
    # e ->  a
    g = NewGraph()
    addVertex(g,'a',[])
    addVertex(g,'b',['a'])
    addVertex(g,'c',['b'])
    addVertex(g,'d',['c','a'])
    addVertex(g,'e',['a'])
    
    print(g)
    print(getVertices(g))
    print(getEdges(g))
