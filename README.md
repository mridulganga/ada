# Algorithms



## Depth First Search Algorithm
### Input: Graph G = (V , E)
### Output: Graph G with its vertices marked with consecutive integers
```
in the order they are first encountered by the DFS traversal
mark each vertex in V with 0 as a mark of being “unvisited”
count ← 0
for each vertex v in V do
  if v is marked with 0
    dfs(v)124
Brute Force and Exhaustive Search
dfs(v)
//visits recursively all the unvisited vertices connected to vertex v
//by a path and numbers them in the order they are encountered
//via global variable count
count ← count + 1; mark v with count
for each vertex w in V adjacent to v do
  if w is marked with 0
    dfs(w)```
