# ReLU(Rectified Linear Unit)
A nonlinear activation function defined as `f(x) = max(0,x)`
If input > 0 , output the input unchanged, if the input < 0, outputs 0;
1. add nonlinearity: convolution and dense layers are linear,
2. sparsity, turn negative inputs into 0, reduces computation and helps prevent overfitting by making the network focus on strong signals.
3. Efficiency, avoid vanishing gradients (unlike sigmoid/tanh)
ReLU is not arbitrary, it's chosen for practical, mathematical reason and bettle-tested.
It's worked from the practice.
