# Intro
Things need to be done not because it's absolutely right or good, just because it have relative value for users.
And this is enough for sell product to the user.

# Cognition
- Deep isn't deeper understanding; rather, stands for successive layers of representations. layered representations learning.
- Learning: a way to measure whether the algorithm is doing a good job is the distance between the algorithm's current output and its expected output, this feedback adjusts the algorithm's performance, which is called learning.
- RSS(Residual sum of squares)
Residual残差， `Mean Squared Error = Rss / n`;
- vector^T
Transpose，
# Concepts
### Gradient
Gradient is a VECTOR that represents the DIRECTION and RATE of the steepest increase of a function.
Each component is a partial derivative, showing how the function changes with respect to (x) and (y);
The gradient points in the direction of maximum increase and its magnitude indicates how steep that increase is.
### Learning Rate(Stepsize)`η`
dynamic learning rate will decrease over time. `α/τ`
- too small would slow converging
- too large would be overshooting, potentially missing the minimum or diverging.
### Gradient Descent
GD is an optimization algorithm commonly used in ML - typically a loss or cost function - by iteratively adjusting the parameters of a model.
1. Objective, a cost function `J(θ)` which variables represent the parameters you want to optimize.
2. Gradient Calculation: gradient the vector of partial derivatives with respect to each parameter. This gradient points in the direction of the steepest increase of `J(θ)`;
3. Step in Opposite Direction: `θ = θ - η*δJ(θ)` which `η` is called `Learning Rate`， a small positive number that controls the step size.
4. Iterate: Repeat the process until the paramters converge to a point where the gradient is near zero or a stopping criterion is met.
### Convergence
stop learning when :
1. changes in J(θ) or θ become negligible
2. after a set number of iterations
3. meet a stopping criterion

### Batch Gradient Descent vs GD
BGD uses the entire dataset to compute the gradient of the cost function in each iteration.
It calculate the gradient by averaging the contributions of all data points.
GD is normally the BGD;
SGD Stochastic Gradient Descent uses just one data point;
Mini-Batch GD uses a small subset of the dataset ;
### Loss or Cost function
cost function is typically the aggregate or average of the loss function over the entire dataset.
# Analytical Approach
it refers to solving a problem - here, finding the optimal parametrs that minimize a loss function - by using exact mathematical formulas, rather than numerical or iterative methods like GD.
### Magnitude
Maganitudes is a scalar value which typically refers to the size or length of the gradient vector, which indicates how steep (steepness) the cost function is at a given point.
It's the Euclidean norm (or length) of the vector;   `∣∇J(θ)∣=(∂J∂θ1)2+(∂J∂θ2)2+…`
#### norm
A norm is a function that measures the size or length of a vector in a vector space.
It's a way to quantify how big or significant a vector is, generalizing the idea of distance or magnitude.
The Edlidean norm is one specific type of norm, commonly used because it corresonds to the straight-line distance we're familiar with in everyday geometry.
A norm is a ruler for vectors.
The norm comes from Latin norma, means a carpenter's square or rule - a tool for measuring or setting a standard. By the 17th century, it evolved in English to mean a standard or pattern .
Norm is neutral, technical term focused on measurement, not authority or personality like King or boss.
In the 19th, mathematicians adopted norm to describe a function that measures size or length in a sonsistent, standardized way, aligning with its meaning as a rule or measure.

### correlation
- correlation
it's relationship between two variables- how they move together .
- coefficient
correlation coefficient is a specific numerical measure that quatifies the strength and direction of the correlation between two variables.
It is the precise metric that measure correlation.
Coefficient is just a number that tells you sth speficic about a relationship .
It's term mathematicians have long used for numbers that describe a specific peroperty or relationship in a formula.

### Bias - Variance
#### Bias
Bias is the error due to overly simple assumptions in the model.

#### Variance
It is the error due to sensitivity to small changes in the training data.
Variance means how much sth changes or varies.
In ML, it's about how much a model's predictions wiggle when you give it slightly different training data.
