# Data augmentation
Data augmentation refers to the action of expanding the dataset by apply some transformations/ processing technique on the current dataset. The methods is used to increase the diversity of the training set and avoid overfitting problem.

## 1. Geometric Transformation
Flip/ Rotation/ Scale/Crop/Translation
Note: 
- The safety of this method refer to its likelihood of preserving the label post-transformation. (i.e: a 6 digit after a rotation could turn to a 9)
- Geometric transformation solve positional/translational biases in the training dataset
- Need to carefully check after do augmentation
Most frequently used: Random cropping, random flipping

## 2. Color Space Transformation
- Solve lighting/color biases in some image recognition problem
- Not always give fancy result since some color change could result in different label
Sample: 
- Color Jittering: We randomly modify the value of brightness, contrast, saturation of the image.

## 3. Add image/noise
- Add Gaussian Noise
"Over-fitting usually happens when your neural network tries to learn high frequency features (patterns that occur a lot) that may not be useful". 
Gaussian noise, which has zero mean, essentially has data points in all frequencies, effectively distorting the high frequency features. This also means that lower frequency components (usually, your intended data) are also distorted, but your neural network can learn to look past that. Adding just the right amount of noise can enhance the learning capability.
- Random erasing
Random select a rectangle in an image and erase its pixel value.
This reduce the risk of overfitting and make model more robust to occlusion

## 4. Deep learning based method
- Use sota GAN(image-to-image translation, i.e: CycleGAN) to generate similar/useful features from the original dataset. 
- In my experience, this method only useful for research purpose/visible problem with large dataset since it is very difficult to well train a GAN when we have little data and very specific type of problem.
