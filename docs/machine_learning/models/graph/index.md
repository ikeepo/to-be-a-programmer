# Graph Concept
A graph is a data structure that represents a set of objects (node or vertex) connected by relationships (edges).
# Concptes
## In Degree
The in degree on a vertex is the number of incoming edges to the vertex.
It counts how many edges point to the vertex from other vertices.
## Out Degree
Number of outgoing edges from that vertex.
### Degree vs Dimension
Dimension means independent;
Degree means some kind of level.

### Edges
- Directed()
  - Cyclic
  - Acyclic(DAG, Dependency Graph)
  relationship ,
  CICD, Make,
- Undirected
- Weighted
- Unweighted
### Node
Don't need to be the same type.
#### Homogeneous
Same type
#### Heterogeneous
Knowledge graphs.
# Representations
## Adjacency List
A collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbours of a node in the graph.
It has direction, each node maps to a list of nodes it points to (outgoing edges).
N nodes have N lists in the list.

## Adjacency Matrix
##

# Use Case
- Asset Correlation
- Programming
# Ref
- [Introduction to Graph Theory](../../../asset/books/graph/IntroductiontoGraphTheory--RichardJ_Trudeau&chenjin5_com--2021--cj5--a817d8e677369f18bcf58b161e46fde4--Anna'sArchive.mobi)
