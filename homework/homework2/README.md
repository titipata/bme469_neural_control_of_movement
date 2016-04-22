# Homework 2

**1. Classifier – back propagation**

Use the code below to create three data clusters which are vertically stacked and therefore not linearly separable, as we discussed in class.  Your job is to create code implementing back propagation for a two layer neural network which can perform this classification.  Use a network with 4 hidden units, as indicated in the shell code. Don’t worry about cross validation and all that – feel free to just use all the data.

```matlab
sd = .85;
x1 = [normrnd(0,sd,50,1); normrnd(0,sd,50,1); normrnd(0,sd,50,1)]; % the input data
x2 = [normrnd(0,sd,50,1); normrnd(5,sd,50,1); normrnd(10,sd,50,1)];
x3 = [ones(150,1)];input = [x1 x2 x3];
output = [ones(50,1) zeros(50,1) zeros(50,1);
          zeros(50,1) ones(50,1) zeros(50,1);
          zeros(50,1) zeros(50,1) ones(50,1)]; % the labels
```

**2. Unsupervised learning – k-means clustering**

In each of the next problems you are given data that appears to be produced by two clusters (use the code in ps1 `datasets.m`, 2a).  Your job in this problem is to use k-means clustering to classify the data according to two clusters. Plot the trajectory of the means as they are updated over iterations, with this trajectory superimposed over the data sets.

```matlab
x1 = [normrnd(0,1,50,1); normrnd(5,1,50,1)]; % the data clusters
x2 = [normrnd(0,1,50,1); normrnd(5,1,50,1)];
input = [x1 x2];
```


**3. Unsupervised learning – ML gradient descent**

Your job is to classify the same dataset as used in problem 2 into two clusters using ML gradient descent to update the values of mean and standard deviation of two Gaussian clusters.  Assume that the prior probabilities of each cluster are already given and fixed at 0.5 each.  
