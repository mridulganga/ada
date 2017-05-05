
graph = [
        [0,2,9999,6],
        [2,0,3,8],
        [9999,3,0,9999],
        [6,8,9999,0]
]
V = 4
weight = [0,2,9999,6]
parent = [0]*V

def findmin(weight,V,visited):
    minv = 9999
    min_pos = 0
    for x in xrange(0,V):
        if visited[x] == False and weight[x] < minv:
            minv = weight[x]
            min_pos = x
    return min_pos

def dij(graph,V):
    visited = [False]*V
    global parent
    global weight

    e=0
    while(e < V):
        u = findmin(weight,V,visited)
        visited[u] = True
        e+=1
        for x in xrange(V):
            if weight[u]+graph[u][x] < weight[x] and visited[x]==False:
                parent[x] = u
                weight[x] = weight[u] + graph[u][x]

def printPath(i):
    print i,
    if (parent[i]!=i):
        printPath(parent[i])

dij(graph,V)
for i in xrange(V):
    print "path : ",
    printPath(i)
    print " weight : " + str(weight[i])
    print ""
