graph = [
    [0,1,1,0],
    [0,0,0,1],
    [0,0,0,1],
    [0,0,0,0]
]
V = 4

visited = [False]*V
queue = []
main_list = []

def bfs(i):
    global visited,queue,main_list,graph,V
    visited[i] = True
    queue.append(i)
    while(queue):
        i = queue.pop(0)
        print i
        for x in xrange(V):
            if (graph[i][x]==1 and visited[x]==False):
                queue.append(x)
                visited[x]=True

bfs(0)
