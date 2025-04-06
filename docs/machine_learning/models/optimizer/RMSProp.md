# RMSProp(Root Mean Square Propagation)
An adaptive learning rate optimization algorithm designed to accelerate gradient descent.
Adjusts the learning rate per parameter based on the magnitude of recent gradients, helping convergence in uneven loss landscapes.
RMSProp modifies standard gradient descent by normalizing the gradient with a moving average of its squared values.
### Propagation
It reflects the algorithm's focus on propagating gradient information over time to adapt the learning process.
The "Propagation" hints at how this mechanism evolves iteratively.

### vs SGD
SGD uses only the current gradient at each step, it's memoryless.
RMSProp adapts the learning rate per weight by propagating gradient information overtime useing a moving average of squared gradients .
