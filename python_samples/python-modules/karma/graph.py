def NewGraph():
    return {}

def addVertex(graph,n,neighbours):
    if len(graph) == 0:
        graph[n] = []
    else:
        if n not in graph:
            graph[n] = []
        for node in neighbours:
            if node in graph and n not in graph[node]:
                graph[node].append(n)
                graph[n].append(node)
                    
def getVertices(g):
    return list(g)

def getEdges(g):
    edges = []
    for k, v in g.items():
        for n in v:
            edges.append((k,n))
    return edges

def printGraph(g):
    for k,v in g:
        print(k+'->[',end='')
        for val in v:
            print(val,end='')
        print(']')
