# Union Find
Disjoint-Set  or Merge-Find, for solving dynamic connectivity problem

# dynamic connectivity problem
Elements are grouped into sets based on connectivity, initially, each element is in its own set.

Dynamic means the connection is removed or added dynamically.


# Disjoint-Set
A data structure used to manage a collection of non-overlapping sets.

Typically implemented using a forest of tree, where each tree represents a set, and the root of the tree is the representative ( or 'parent') of the set.



# Union
It merges two sets (groups of elements) that contain the given elements, regard of there values or types.

Not about identical, could be different, Union simply groups their sets together.


# Find
It identifies the representative(or root) of the set that an element belongs to.

If two elements have the same root, Find returns the same value for both.

Not about identical too. Just find element's root.
### Path Compression
Optimization for Find, flatten tree structure of a set duing a Find operation.


# Procedure
- MakeSet(x): x as its own set root and rank 0

- Find: determine which set an element belongs to

- Union: Merge two sets into the root of the tree with higher rank. If the rank of two sets are same, choose one and increment its rank.
