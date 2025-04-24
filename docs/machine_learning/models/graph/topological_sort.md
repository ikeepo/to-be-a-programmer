# Topological Sort
An algorithm that orders the vetices of a directed acyclic graph.
# Complexity
 O(V + E)
The Algorithm processes each vertex, and at every vertex, processing every neighbor which is Edge.
## What if there is a internal iteration on processing every node
The internal iteration has a constant cost (K), `O(KV)` still `O(V)`

# Approaches
## Kahn's Algorithm
Vertices with in-degree 0 has no dependencies and can be processed first.
When a vertex is processed, the in-degrees of its neighbors are decreased, simulating the removal of its dependencies.
## DFS
