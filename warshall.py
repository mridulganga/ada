V = 4

def floydWarshall(graph):
    dist = graph

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if (dist[i][j]==0 and dist[i][k]==1 and dist[k][j]==1):
                    dist[i][j] = 1

    printSolution(dist)

def printSolution(dist):
    print "Final Matrix"
    for i in range(V):
        for j in range(V):
            print "%7d\t" %(dist[i][j]),
        print ""

graph = [[0,1,0,1],
         [0,0,1,0],
         [0,0,0,1],
         [0,0,0,0]
        ]
# Print the solution
floydWarshall(graph);
