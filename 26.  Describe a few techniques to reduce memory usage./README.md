26.  Describe a few techniques to reduce memory usage.

- Remember to use properly data type. Take advantage of data range. For example: image data is from 0-255 -> use unsigned char instead of int. Consider doing computation in a less memory way (quantization)
- For C++: use dynamic memory allocation, smart pointer
- For Python(specially training dnn): 
Use local object instead of global ones
Load into batch instead of data chunks
Use library instead of write code from scratch could help if you not familiar with memory management in python
when building dnns, consider use in-place activation
Finally, limit/change the input size could help too.