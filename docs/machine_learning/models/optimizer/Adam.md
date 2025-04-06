# Adam(Adaptive Moment Estimation)
A popular optimization algorithm combining momentum and RMSProp.
## Why Adam
- Fast convergence, adapts learning rate per parameter.
Parameter refers to the trainable weights of your neural network.
Parametr refers to each scalar value within weight vectors.
- Robust;
- Momentum Boost
Momentum is a technique from physics-inspired optimization that accelerates gradient descent by adding "inertia" to weight updates, help them moving faster along consistent direction.
Momentum boost in Adam refers to Adam's use of a moving average of gradients (called m), which gives updates a push based on past gradient directions, not just the current step.
`m_t = β1 * m_{t-1} + (1 - β1) * g_t`
Momentum means the gradient average.
`β1 = 0.9` `β1` is the **decay rate**(smoothing factor) in the EMA . default empirical value.
EMA weights all past steps, decaying exponentially `0.1 * (g_t + 0.9*g_{t-1} + 0.81*g_{t-2} + ...`
## 为什么要指定学习率
既然是自适应，因为自适应调整的是相对步长，但是绝对步长仍由learning rate决定；
