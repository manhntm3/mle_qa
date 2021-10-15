## DeepStream 
When deploy AI models on embedded devices, even with specific hardware and optimizer, we still can meet some I/O bottleneck. Especially when we deal with complex I/O pipeline and models with multiple inputs and outputs, the process will take a lot of time and impossible to reach real-time processing.
DeepStream is a SDK developed by Nvidia, contains many hardware accelerator plugins to compute graphic heavy operations. 
- DeepStream can achieve highest performance for video analytic applications. 
- DeepStream is optimized for nvidia gpus, embedded edge device Jetson platform

## TensorRT

A SDK developed by Nvidia for fast inference on nvidia GPUs. Built on CUDA, TensorRT could speed up inference time around 4 - 5 times on real-time devices and embedded apps.
TensorRT operates in two phases:
- The Build Phase: Provide TensorRT with model definition and TensorRT optimizes it for a target GPU
- The Runtime Phase: Optimize model for inference
How TensorRT optimize:
- Weight and Activation Precision Calibration
- Layers and Tensor Fusion
- Kernel auto-tuning
- Dynamic Tensor Memory
- Multiple Stream Execution

## Different between DeepStream and TensorRT
- DeepStream was built on top of many nvidia library such as TensorRT, cuda,...
- TensorRT is just for the DNNs inference part. The other part, e.g: image read, conversion, osd, render, etc... are provided by DeepStream

Reference sources:
TensorRT docs:
https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#overview
DeepStream docs:
https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Overview.html

https://medium.com/@abhaychaturvedi_72055/understanding-nvidias-tensorrt-for-deep-learning-model-optimization-dad3eb6b26d9
https://towardsdatascience.com/how-to-deploy-onnx-models-on-nvidia-jetson-nano-using-deepstream-b2872b99a031
