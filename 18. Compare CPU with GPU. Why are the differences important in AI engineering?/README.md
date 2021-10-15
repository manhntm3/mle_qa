Compare **CPU** with **GPU**. Why are the differences important in AI engineering?

CPU: central processing unit
Designed to handle wide-range of tasks quickly, but CPU is limited to the concurrency of tasks that can be running. Can have 8 or 16 cores for perform calculation.

GPU: graphic processing unit
Designed to render image/video where parallelism matters(split into region and render in parallel). With thousand of processor cores running simutaneously, GPU enable massive parallelism and extensive computing power for tasks which can be devided into small parts (repetitive and highly-parallel tasks).

Particularly, in AI engineering, computational resources is a key factor to demonstrate the power of ML, computer vision algorithm. Most AI system, especially deep learning based system, require a lot of data sample to be able to produce an acceptable output. While running, as we split the data to batches to fit the memory, GPU has advantage over CPU because the computation could be done in parallel. In practice, this could save up huge amount of the time used for training/evaluating model.

Some note:
- For training, GPU is ideal
- Most of program load data from disk to RAM and move to GPU for computation. Because CPU behave concurrently, there could be a bottleneck when moving the data
- For inference/production mode, although GPU and CPU could handle a wide-range of computation (i.e: matrix multiplication, sigmoid,..) and yield a similar output, the way its handle varies on different hardware. This is because each CPU/GPU has its own instruction sets. Normally, CPU has smarter and wider instruction sets(for example: it support int8 computing), so if the AI model is simple and small, running inference on the CPU is more economical since GPU is more expensive.


Reference Sources:
https://www.omnisci.com/technical-glossary/cpu-vs-gpu
https://www.intel.com/content/www/us/en/products/docs/processors/cpu-vs-gpu.html
https://developer.nvidia.com/blog/gpudirect-storage/
https://medium0.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fwhat-is-a-gpu-and-do-you-need-one-in-deep-learning-718b9597aa0d
https://www.avnet.com/wps/portal/silica/resources/article/fpga-vs-gpu-vs-cpu-hardware-options-for-ai-applications/