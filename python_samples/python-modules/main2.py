import karma.graph as gph

if __name__ == '__main__':
    g = gph.NewGraph()
    gph.addVertex(g,'a',[])
    gph.addVertex(g,'b',['a'])
    gph.addVertex(g,'c',['b'])
    gph.addVertex(g,'d',['c','a'])
    gph.addVertex(g,'e',['a'])
    
    print(g)
    print(gph.getVertices(g))
    print(gph.getEdges(g))

