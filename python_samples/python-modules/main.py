import karma.graph as graph

if __name__ == '__main__':
    g = graph.NewGraph()
    graph.addVertex(g,'a',[])
    graph.addVertex(g,'b',['a'])
    graph.addVertex(g,'c',['b'])
    graph.addVertex(g,'d',['c','a'])
    graph.addVertex(g,'e',['a'])
    
    print(g)
    print(graph.getVertices(g))
    print(graph.getEdges(g))
