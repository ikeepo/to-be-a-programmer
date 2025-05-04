# Kadane's Algorithm
## What: A precise specification of the problem that the algorithm solves.
Maximum Subarray sum problem.

#### What Concepts it has, define them in human/math/rust language
##### `max_so_far`

`max_so_far` returned value, easy to understand.

##### `max_ending_here`

`max_ending_here` maximum of subarray ends at the current index.
`max_ending_here` is the local maximum, the `max_so_far` is the global maximum.
$$max_ending_here = max(max_ending_here+a[i], a[i])$$
eliminating the starting sub-subsequence with negative sum, starting from the positive one immidiately. Only in this condition would choose `a[i]`

if max_ending_here is negative, discarding it then start from here.

$$max_so_far = max(max_so_far, max_ending_here)$$

#### What Problem it deal with
#### What Condition it use?
#### What Property it has?
## How: A precise description of the algorithm itself.
## Why: A proof that the algorithm solves the problem it is supposed to solve.
It used `contiguity` to implement a dynamic programming-type algorith.

There are two conditions:

First is a maximal adjacent subsequence cannot have a starting subsquence with a negative sum.

## History: when it is proposed, how it envolved.
Developed by Joseph Kadane in the late 1970s; Formal artical is a recounted one published by Kadane in 2023;



## How fast: An analysis of the running time of the algorithm
O(n);

# [Refs](../../refs.md#algorithm)

[^1]: [Two Kadane Algorithms for the Maximum Sum Subarray Problem.2023](https://www.mdpi.com/1999-4893/16/11/519)
