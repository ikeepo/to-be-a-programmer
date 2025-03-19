# GMM(Gaussian Mixture Model)
A GMM assumes your data is generated from a mixture of several Gaussian(normal) distribution;
## random_state
It controls the randomness involved in the algorithm.
It is a seed for the random number generator used by the Gaussian Mixture Model algorithm, It ensures that any randomness in the process is reproducible.
## Posterior Probability
For GMM ,it means for each sample,`predict_proba` calculates the probability that it belongs to each of the two components, given the fitted model.
POSTERIOR here means it's conditioned on the data and the model parameters after training with gmm.fit()
