# Topological Sort
An algorithm that orders the vetices of a directed acyclic graph.
Dependency resolution order for DAG.


# Complexity
 O(V + E)
The Algorithm processes each vertex, and at every vertex, processing every neighbor which is Edge.
## What if there is a internal iteration on processing every node
The internal iteration has a constant cost (K), `O(KV)` still `O(V)`

# Approaches
## Kahn's Algorithm
Vertices with in-degree 0 has no dependencies and can be processed first.

### Procedure
1. calculate in-degree of all nodes
2. put all in-degree 0 into queue
3. while q => process current node (in-degree 0 node)
3.1 label current node visited
3.2 in-degree of neighbors decrease
3.3 neighbor in-degree to 0, push into queue
3.4 check constrain condition

### Process Rule
since the element pushed queue is in-degree 0, so the process's purpose is make neighbor in-degree 0;
the in-degrees of its neighbors are decreased, simulating the removal of its dependencies.
queue only process in-degree 0 makes sure every node can only be processed once.
In-degree 0 means on dependency.

There are two parts:
- Current Node
- Neighbors
某种变换，变换后可以成为CurrenNode状态以push到queue中；
## DFS
