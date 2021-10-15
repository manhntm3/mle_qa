
# Machine Learning models in general
### 1.Continuous Learning
ML models was built and designed based on the assumption in which training sample and testing data will be somewhat similar(i.e: share the same distribution/latent space). While some ML model can retain this condition with extensive training data, most real-world AI application require dynamic data environment where data is constantly changing over time. This create an implicit "drift" in ML models and an accuracy decrease with new sample come from new environment/settings that not in the training set. 
ML models needs to be trained regularly to address this issue. 
The key point is how to select data for training. Important thing to notice:
- How the new data coporate/corelated with old data ? In other words, do an analysis on the evolution of data over time to observe the drift in data.
- Level of retraining ? Do we just refitting model with new data ? In ensemble model, do we need to train the whole models or just a part of it?
- The resources we need for continuous development (GPU/CPU/cloud,...) ? 

# Deep Learning models
### 1. Optimize model objective function through gradient(How to train)
Gradient Descent: Most widely used method for training neural networks. The methods ultilized gradient to find a local minimum. Iteratively, it compute the gradient change in objective loss with respect to the weight and let the weight drive towards the opposite direction since it will be the steppest descent toward local minimum. Formally, it can be describe by this function: 
W = W - alpha * derivative(J) with respect to W
Some development in GD:
- stochastic gradient descent: use single sample to compute gradient/update w
- mini-batch gradient descent: use single batch to compute gradient/update w
- momentum gd: use history to calculate velocity(direction of the gradient)
velocity = previous update * momentum + lr * gradient
param = param - velocity 
Some other methods: Adam, RMSpop (ulitilize moving averages)
Recently: LAMB

### 2.Transfer learning
"Transfer learning is the improvement of learning in a new task through the transfer of knowledge from a related task that has already been learned"
In practice, transfer learning refer to the use of pretrain model that very well-trained on large dataset(i.e: ImageNet), retrain it with very low learning rate on a specific dataset.  
- Transfer learning works when the base dataset/task is more general or highly related to the specific task. The base dataset should not contain sample specific to the base task
- How transfer learning works ? 
With the use of base dataset, the base model has already learn how to extract useful information instead of from scratch. For example, in the field of object classification, when we use ImageNet pretrained models, at the begining of the network, the models has already learn how to distinguish edges, curves, ...(low/mid level feature) and perform very well in generalization. This knowledge then can be transfered to the new model efficiently. This allow new training model focus on high level/ complex feature on specific task and achieve more accuracy.

- When to use it?
Unless the task is very specific or use a new network achitecture, most of the time transfer learning is the first thing we should try. We must have pretrained version of the network available online(again, this model should be well-trained by giant tech company like Google, Nvidia, FB, ...). This is because when we start normally we don't have sufficient amount of data at hand. If we have enough data, we can train from scatch and expect a very slighly improvement.

### 3. Knowledge Distillation

Train a compact neural network using the distill knowledge extrapolated from a larger model or ensemble model. 
The bigger model is usually called the teacher, the target model is called student.
Why it works? The bigger model provide much more information(high entropy) than the data. (think about classify a deear, a horse and a ship)

Soft target: the loss computed out of teacher's prediction, usually use softmax with temperature T
Hard target: ground truth
Loss is computed as blending of two loss (hard target and soft target)