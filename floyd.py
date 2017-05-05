V = 4

INF  = 99999
def floydWarshall(graph):
    dist = graph

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])

    printSolution(dist)

def printSolution(dist):
    print "Shortest Paths"
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print "%7s" %("INF"),
            else:
                print "%7d\t" %(dist[i][j]),
        print ""

graph = [[0,5,INF,10],
         [INF,0,3,INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
        ]
# Print the solution
floydWarshall(graph);
