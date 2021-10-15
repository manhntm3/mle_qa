12.  How to stabilize an arbitrary blurry or shaky video?

Video Stabilization
If we have the camera information during recording, we could use mechanical or optical video stabilization, which will yield better results. But normally we will just have the video itself.
So in digital video stabilization, 3 main steps:
- Motion estimation: Find the transformation parameters between two consecutive frames 
- Motion smoothing: Smooth out transformation by filtered out unwanted motion
- Image composition: Construct stabilized video

We can extract high level features (e.g: SIRF in OpenCV). Then build feature either bruteforce way or KD-Tree (also in OpenCV), then match each two consecutive frames to find pairs of corresponding features. Last, we should get geometric transformation matrix which is minimize error of transformed points. Feed those pairs into cvFindHomography to compute the homography between those frames. Warp frames according to (combined..) homographies to stabilize.