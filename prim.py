graph1 = [
    [0,2,3,0],
    [0,0,0,4],
    [0,0,0,1],
    [0,0,0,0]
]
V1 = 4

graph2 = [[0, 2, 0, 6, 0],
          [2, 0, 3, 8, 5],
          [0, 3, 0, 0, 7],
          [6, 8, 0, 0, 9],
          [0, 5, 7, 9, 0],
         ]
V2 = 5

def findmin(key,visited,V):
    minv=9999
    min_pos=0

    for x in xrange(V):
        if (visited[x]==False and key[x] < minv):
            minv = key[x]
            min_pos=x
    return min_pos


def prim(graph,V):
    #Initialise some arrays
    parent = [0]*V
    key = [9999]*V
    visited = [False]*V

    #first key value
    key[0] = 0
    parent[0] = 0

    for e in xrange(V-1):
        i = findmin(key,visited,V)
        visited[i]=True
        for x in xrange(V):
            if (graph[i][x]>0 and visited[x]==False and graph[i][x] < key[x]):
                key[x] = graph[i][x]
                parent[x] = i

    for i in xrange(1,V):
        print parent[i],i,graph[parent[i]][i]



prim(graph2,V2)
