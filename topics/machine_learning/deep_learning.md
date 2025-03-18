# Axon
An Axon is a long, thin part of a neuron that carries electrical signals away from the cell body to other neurons.
A synaptic connection is the junction where one neuron communicates with anohter.
It's where the signla from an axon ( from the sending neuron) passes to the dendrites or cell body of the recoiving neuron.
# Perceptron
It's the simplest artificial neuron model. Takes multiple inputs , each with a weight, computes a weighted sum, applies an activation function(step function) to classifies inputs into two groups.
MLP is made of multiple layers of Percptrons. It has an input layer, hidden layers, and output layer.
Uses backpropagation with gradient descent to adjust weights and minimize error.

# Activation Function
They take the weighted sum of inputs and transform it into an output.
- Step Function   output binary
- Sigmoid
- Tanh
- Linear Function
## Why it's called activation
In a real neuron, and action potential is triggered when the input signal crosses a threshold.
## Error Propagation
Error Propagation refers to the process of calculating and distributing the error (difference between predicted and actual outputs) backward through a neural network to update its weights.
It's how the network learns from mistakes.
The error starts at the output and flows back to earlier layers, telling each neuron how much it contributed to the mistake.
## Learning rate is same across all layers and inputs within one iteration
Learning Rate is the step size in gradient descent, controlling how much weights change.
During backpropagation, the rror propagates from the output layer back to the input layer.
The same η is applied to update all weights across all layers in that single update step;
Each weight gets its own gradient, but η sets the overall pace.
# One Hot Encoding / Dummy Encoding
OHE is a way to convert categorical variable into a binary vector where each category gets its own column, and only one column is "1"(Hot) while the rest are "0";
dummy encoding is similar to OHE, but it uses n - 1 columns for (n) categories, dropping one category as a reference(baseline).
dummy encoding has fewer columns.
In statistics, "dummy variable" is a stand-in (or placeholder) for a categorical value.
dummy means fake or substitude.
When modeling categorical data, statisticians created binary variable to "stand in" for these categories.  They called them "dummy variable" to distinguish them from continuous variables.
# CNN
Convolutional neural network;
Comes from the mathematical operation called convolution.
Convolution is a way to "slide" a small window (called a FILTER or KERNEL) over a larger input (like an image) to detect patterns, blending the filter's values with the input's values at each step.
In mathematics and signal processing (19th century), where convolution combines two functions to show how one modifies the other.
# RNN Recurrent neural networks
Output of one step is fed back as input to the next step, allowing it to maintain a "memory" of previous inputs.
Recurrent means "to run back" or "to return";
# Gradient vanishing
Gradient vanishing happens when the gradients become extremely small as they propagate backward through layers or time steps.
# Gradient exploding
Gradients become extremely large.
