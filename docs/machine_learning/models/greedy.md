# Greedy Algorithm
At each decision point, it chooses the option that looks best right now, without worrying about how it affects future steps.
It doesn't always gurantee the absolute best overall solution.
## Why Greedy
##### Short_slighted
It optimizes locally (one node) without planning the global tree struture.
##### Contrast
A non-greedy approach might test all possible trees (exponential time) to find the absolute best, but that's impractical.
# Greedy in GBDT and LightGBM
- Each decision tree uses a greedy algorithm to grow
- At each node, it picks the slit that best reduces the loss
- LightGBM's leaf-wise growth is extra greedy: it only splits the leaf with the biggest potential gain, not all leaves at a level.
# The initial feature split has a big influence on the tree's structure and predictions
The initial feature shapes the tree.
Greedy Bias, Path dependency.
## How to Avoid
- Feature Enginnering
Create better features to make the root split more meaningful.
- Limit Tree Depth
A shallow tree relies less on the root split, reducing its dominance.
- Ensamble Methods
A single tree's wrong split is corrected by the ensemble.
- Randomness
`feature_fraction` in LightGBM randomly consider only a subset of features at each split.
- Regularization
