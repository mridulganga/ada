def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

def union(parent,rank,x,y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

def KruskalMST(graph,V):

        result =[] #This will store the resultant MST

        i = 0
        e = 0

        graph =  sorted(graph,key=lambda item: item[2])

        parent = [] ; rank = []
        for node in range(V):
            parent.append(node)
            rank.append(0)

        while e < V -1 :
            u,v,w =  graph[i]
            i += 1
            x = find(parent, u)
            y = find(parent ,v)

            if x != y:
                e += 1
                result.append([u,v,w])
                union(parent, rank, x, y)


        print "Minimum Spanning tree"
        for u,v,weight  in result:
            print ("%d -- %d == %d" % (u,v,weight))
graph=[]
graph.append([0, 1, 10])
graph.append([0, 2, 6])
graph.append([0, 3, 5])
graph.append([1, 3, 15])
graph.append([2, 3, 4])

V = 4

KruskalMST(graph,V)
