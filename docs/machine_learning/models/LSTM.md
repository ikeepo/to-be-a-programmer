# LSTM
## Not Fully Connected Layer
At each computation, every input is connected to every unit.
The LSTM layer as a whole only connects to the input of the current time step (xt) and the previous hidden state, rather than to the inputs of all time steps simultaneously.
