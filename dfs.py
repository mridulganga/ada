graph = [
    [0,1,1,0],
    [0,0,0,1],
    [0,0,0,1],
    [0,0,0,0]
]
V = 4

visited = [False]*V
stack = []
main_list = []

def dfs(i):
    global visited,stack,main_list,graph,V
    visited[i] = True
    stack.append(i)
    for x in xrange(V):
        if (visited[x]==False and graph[i][x]==1):
            dfs(x)
    main_list.append(stack.pop())

for i in xrange(V):
    if (visited[i]==False):
        dfs(i)

print main_list[::-1]
