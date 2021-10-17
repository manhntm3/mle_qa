Compare **YOLOv4** with **YOLOv5**.

All YOLO family are in a type of Single Stage Detector which make a fixed number of prediction on grid (one stage), focus more on speed and optimize accuracy after. 

YOLOv4
https://arxiv.org/abs/2004.10934
https://github.com/AlexeyAB/darknet
Architecture

YOLOv5

6.  Compare **YOLOv4** with **YOLOv5**.
    
7.  Compare **YOLOv4** with **ScaledYOLOv4**.
    
8.  Is running a large image through a **YOLO** model slower than running many small images through it?

Yes. Image go through YOLO model will have the input size is a multiple of 32. Larger images means more predictions and more computaionally expensive thus slower.