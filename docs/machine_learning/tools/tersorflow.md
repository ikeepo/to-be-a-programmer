# TensorFlow
# Sequential
Sequential is a keras class for creating a linear stack of layers.
The stack here reflects both the conceptual and technical design of how this Keras class works.
1. Linear, Ordered Structure
A stack implies a strict, sequential order where layers are piled one on top of the other.
2. In dl, we often think of networks as having depth, with layers stacked vertically in diagrams.
# Faltten
A keras layer that transforms a multi-dimensianl input into a 1D vector.
It collapses all dimensions except the batch size into a single dimension .
It's a purely a format change - it reshapes the data without any mathematical calculations.
# Dense
A fully connected layer in Keras where every input neuron connects to every output neuron.
Each of the 50 neurons computes a weighted sum of all 832 inputs, adds a bias, then applies ReLU.

# `model.compile`
A keras method that configures the model for training by specifying how it will learn and evaluate performance.
