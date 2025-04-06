# [LightGBM](https://en.wikipedia.org/wiki/LightGBM)([Light Gradient-Boosting Machine](https://lightgbm.readthedocs.io/en/stable/)) [code](https://github.com/microsoft/LightGBM/tree/master/examples/binary_classification)
It was originally developed by Microsoft and first introduced in 2016 as part of their efforts to advance gradient-boosting techniques for large-scale data processing.
The framework builds on the foundation of earlier gradient-boosting methods, such as Gradiet Boosting Decision Tree (GBDT), but incorporates innovative approaches to overcome their limitaions, particularly in terms of speed and memory usage.
The development of LightGBM was motivated by the need for a faster and more scalable alternative to existing boosting frameworks like XGBoost(2014).
First stable version was released in 2017 with paper titled "[LightGBM: A Highly Efficient Gradient Boosting Decision Tree](https://proceedings.neurips.cc/paper_files/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf)"
The LightGBM framework supports : GBT, GBDT, GBRT, GBM, MART and RF.
## Key Innocative Work
What makes LightGBM special isn't a variety of algorithms but its optimization to GBDT;
##### Gradient-Based One-Side Sampling
##### Exclusive Feature Bundling
##### LightGBM adopts a leaf-wise tree growth strategy rather level-wise approach
This decides that how you customize GBDT's behaves for your task by setting: Objective function and Hyperparameters.

## Concepts
##### why it's called framework rather model
It's a system that enables the creation of gradient-boosting models, not a single, specific model itself.
LightGBM provides the algorithms, data-handling capabilities, and customizable settings that let users build and train their own gradient-boosting decision tree models for tasks like classification or regression.

##### gradient-boosting technique


##### large-scale data
##### What LightGBM is built around a single core algorithm mean
LightGBM is fundamentally based on one algorithm: GBDT. It's the engine under the hood.
# Practice
## [Install](https://lightgbm.readthedocs.io/en/stable/Installation-Guide.html#linux)
