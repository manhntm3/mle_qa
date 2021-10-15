How to run a PyTorch model in a C++ program?

The original ways (Pytorch way):
- Pytorch C++ frontend: highlevel, pure C++ modeling interface for neural network and general ML research. This enable define & training models purely in c++. Personally, I think this is only used for research purpose since writing neural network training in C++ is much more difficult than Python, even though c++ run x2 faster
- TorchScript: TorchScript is a representation of Pytorch model that can be understood, compile and serialized by Torch Script compiler, in other words, can be loaded and executed purely from C++ with no dependency in Python.

  Basically, we will define & training our model in python, convert into TorchScript model, serialize and save it to a file. On the targeted environment, build LibTorch(Pytorch C++ API), include it in your project and run inference in c++. Follow this tutorial for more details: https://pytorch.org/tutorials/advanced/cpp_export.html
  
Some other way to run Pytorch model in c++:
- In my experience, LibTorch is quite slow and error-prone when it run on some devices. 
Since Pytorch is impressively huge and transfer, optimise code from python to C++ is not easy lol :))
So we could use more simple, dedicated frameworks to run model than the original LibTorch. The process is we still define & training our model in Pytorch, convert it to a specific framework that we use and then run inference on that framework using C++ API.
Two example is TensorRT(GPU device) and NCNN(Mobile device):
Pytorch Model -> Onnx -> TensorRT 
Pytorch Model -> Onnx -> Nccn

Reference Sources:
https://pytorch.org/cppdocs/

