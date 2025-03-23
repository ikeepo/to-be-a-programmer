# Comcepts
##### shuffle
Weather the data is randomly shuffled before being split into training and test sets.
# [Skewness and Kurtosis](https://www.simplilearn.com/tutorials/statistics-tutorial/skewness-and-kurtosis)
Under the influence of significant causes, the normal distribution can get distorted.
The distortion can be calculated using skewness and kurtosis.
Skewness refers to the degree of symmetry, or more precisely, the degree of lack of symmetry;
Positively Skewed: the values are more concentrated towards the right side;
Negatively Skewed: the data points are more concentrated towards the left side;
Kurtosis refers to the proportion of data that is heavy-tailed or light-tailed in comparison witha  normal distribution.
Positive Kurtosis: light tailed
Negative Kurtosis: heavy tailed, like punching the distribution;

### [zero skew: mean = median](https://www.scribbr.com/statistics/skewness/)

# correlation
### Rule of Thumb
0.00–0.19: Very weak.

0.20–0.39: Weak.

0.40–0.59: Moderate.

0.60–0.79: Strong.

0.80–1.00: Very strong.
# Data Leakage
Use scaler trained by train data to transform test data to avoid test set's mean and standard deviation would influence the scaling, "leaking" information from the test set into the preprocessing step .
# zip()
the word zip means to fasten or join two things together quickly, like closing a zipper on a jacket. It aligns two rows of teeth into one unified strip.
# R2
R-squared, evaluate the performance of a regression model.  range from 0-1,
`R^2=1 - SS_res / SS_tot`
SS_res means sum of the squared redisuals (differnce between actual and predicted values)
SS_tot means sum of squares (variance of the actual data from its mean)
# Confusion Matrix
Classification metrics;
A CM compares `predicted discrete labels` to  `actual discrete labels`, counting how often predictions match or deviate from the truth.
# Accuracy Score
The proportion of correct predictions out of all predictions.
# Precision Score
The proportion of true positive predictions out of all positive predictions made by the model;
# Recall Score
The proportion of true positives identified out of all actual positives;
# Fl Score
The harmonic mean of precision and recall;
`F1 = 2 * (Precision * Recall) / (Precision + Recall)`
Harmonic mean is a type of average that's particularly useful when dealing with rates, ratios or quantities that are inversely related.
HM empasizes smaller values.
Harmonic is a balancing act. It doesn't let a model check bby excelling in one metric while failing in another.  And sensitivity to weakness.
Harmonic because it's derived from the reciprocals , and the reciprocal nature is what makes it sensitive to smaller values.
Harmonic origins from Greek harmonikos meaning sklled in music or relating to harmony.
Everyday sense: something harmonic suggests balance, agreement, or a pleasing arrangement, like in music where harmonics are tones that resonate together smoothly.
**Harmonic means working together in a balanced, reciprocal way.**
# [ROC Curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
Receiver Operating Characteristic curve.
Receiver refers to a signal receriver in early radar and communication systems.
Operating how the receiver functions as you adjust its decision threshold;
Characteristic the trade-off between detecting true signals(True Positive Rate) and false alarms (False Positive Rate);
So, Receiver Operating Characteristic literally means the characteristic performance of a receiver in operation, reflecting its ability to distiniguish signal from noise across different settings.
ROC Curve is a plot of TPR vs FPR as you adjust the decision threshold.
Threshold means predict 1 only if prob > threshold;
It's like a tuning knob for model;
# Seasonal Decompose
