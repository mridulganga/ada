# Algorithms



## Depth First Search Algorithm
#### Input: Graph G = (V , E)
#### Output: Graph G with its vertices marked with consecutive integers
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
    dfs(w)
```

## Breadth First Search
#### Input: Graph G = V , E
#### Output: Graph G with its vertices marked with consecutive integers
```
in the order they are visited by the BFS traversal
mark each vertex in V with 0 as a mark of being “unvisited”
count ← 0
for each vertex v in V do
  if v is marked with 0
    bfs(v)
bfs(v)

//visits all the unvisited vertices connected to vertex v
//by a path and numbers them in the order they are visited
//via global variable count

count ← count + 1; mark v with count and initialize a queue with v
while the queue is not empty do
  for each vertex w in V adjacent to the front vertex do
    if w is marked with 0
      count ← count + 1; mark w with count
      add w to the queue
remove the front vertex from the queue
```

## Insertion sort
#### Input: An array A[0..n − 1] of n orderable elements
#### Output: Array A[0..n − 1] sorted in nondecreasing order
```
for i ← 1 to n − 1 do
  v ← A[i]
  j ← i − 1
  while j ≥ 0 and A[j ] > v do
    A[j + 1] ← A[j ]
    j ← j − 1
  A[j + 1] ← v
```


## Binary Search
#### Input: An array A[0..n − 1] sorted in ascending order and a search key K
#### Output: An index of the array’s element that is equal to K or −1 if there is no such element
```
l ← 0; r ← n − 1
while l ≤ r do
  m ← (l + r)/2
  if K = A[m] return m
  else if K < A[m] r ← m − 1
  else l ← m + 1
return −1
```

## Merge sort
```
// Merge Sort Algorithm
//Input: An array A[0..n − 1] of orderable elements
//Output: Array A[0..n − 1] sorted in nondecreasing order
if n > 1
  copy A[0..n/2 − 1] to B[0..n/2 − 1]
  copy A[n/2..n − 1] to C[0..n/2 − 1]
  Mergesort(B[0..n/2 − 1])
  Mergesort(C[0..n/2 − 1])
  Merge(B, C, A) //see below

// Merge Algorithm
//Input: Arrays B[0..p − 1] and C[0..q − 1] both sorted
//Output: Sorted array A[0..p + q − 1] of the elements of B and C
i ← 0; j ← 0; k ← 0
while i < p and j < q do
  if B[i] ≤ C[j ]
    A[k] ← B[i]; i ← i + 1
  else A[k] ← C[j ]; j ← j + 1
  k ← k + 1
if i = p
  copy C[j..q − 1] to A[k..p + q − 1]
else copy B[i..p − 1] to A[k..p + q − 1]
```


## Quick Sort
```
// Quicksort Algorithm
//Input: Subarray of array A[0..n − 1], defined by its left and
right indices l and r
//Output: Subarray A[l..r] sorted in nondecreasing order
if l < r
  s ←Partition(A[l..r]) //s is a split position
  Quicksort(A[l..s − 1])
  Quicksort(A[s + 1..r])

// Partition Algorithm
//Input: Subarray of array A[0..n − 1], defined by its left and
right indices l and r (l < r)
//Output: Partition of A[l..r], with the split position returned
as this function’s value
p ← A[l]
i ← l; j ← r + 1
repeat
  repeat i ← i + 1 until A[i] ≥ p
  repeat j ← j − 1 until A[j ] ≤ p
  swap(A[i], A[j ])
until i ≥ j
swap(A[i], A[j ]) //undo last swap when i ≥ j
swap(A[l], A[j ])
return j
```

## Heap Sort
