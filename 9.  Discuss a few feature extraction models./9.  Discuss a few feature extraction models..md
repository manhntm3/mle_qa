9.  Discuss a few feature extraction models.
## ResNet
Develop by Microsoft in 2015. 
Basically ultilize the idea of ResNet block to solve the problem of vanishing gradient, that is after computing backpropagation, the gradient become smaller and smaller at the later layer.
ResNet Block
Add a residual connection from the input to the end, concat with the output of convolutions and go through relu activation. (F(x) + x)
Notice: This kind of design requires that the output of the convolutional layers has to be of the same shape as the input, so that they can be added together. If we want to change the number of channels, we need to introduce an additional 1×1 convolutional layer to transform the input into the desired shape for the addition operations.
ResNet has many public pretrained model on internet and recieve great interest since it can scale from ResNet-18 to ResNet-101 with bigger model achieve higher accuracy.

## VGG Net
Develop by Oxford Uni. 
It contain many small kernel convolution to reduce the number of parameters (e.g: one 5x5 could replace by two 3x3). So it's very useful in application like: Text Detector, Small Object Detector

## MobileNet
Develop by Google. 
Mostly used in application which focus more on speed with limited resources. Utilize the ideal of depthwise separable convolution and width multiplier.
depthwise separable convolution: contain a depthwise convolution: compute convolution for each channels and a pointwise convolution: a 1x1 convolution to compute the sum of previous depthwise conv.
This largely reduce the number of computation need for perform feature extraction.
Width multiplier: Just a parameter to control input resolution for each layer of the network. Higher wd means high accuracy and bigger model.

## Autoencoder
A deep learning architecture which try to stimulate input. that is try to find a function f(x) =x. It split into two parts:
encoder: takes the input data and compress it, so that to remove all the possible noise and unhelpful information. The output of the encoder stage is usually called bottleneck or latent-space.
decoder: take the encoder output and decompress it, reproduce or generate output so that it replicate the input as much as possible. 
Normally, we will train both encoder and decoder so that it become more easy to train and then remove decoder for feature extraction


In research, there also a hot topic call Neural Architecture Search which try to find a way to find the best deep learning architecture for specific problem. https://github.com/mit-han-lab/once-for-all





