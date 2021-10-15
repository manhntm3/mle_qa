## Aruco
Aruco is a type of fiducial marker. Fiducials are special markers we place in the view of the camera such that they are easily identifiable. 
Normally, Aruco contains uniquely 2D binary pattern that computer vision system can easily detect. Because of that, put them in the realworld could support the the system could make decision/request regardless changes in the viewpoint, distortion,...

For example we could add an Aruco to the corner of an frame in the scene. Then we could capture the entire scene and replace the picture frame with arbitrary video or image. We don't have to worried so much about perspective distortion when the viewpoint of the camera changes.

Use in many applications: calibration, robotics, measurement,...

## Aruco vs AprilTag vs QR

Aruco and AprilTag are the same type of fiducial marker(I will list the different later). QR, on the other hand, is use for compress/request useful information. So the QR code normally contain more than 3KB of data, while marker like Aruco only contain simple pattern, holds only 4-12 bits of data. This also help Aruco simple and easily detect and identify when we camera at longer range.

Aruco vs AprilTag

AprilTag usually use in RosSystem since it come with an implementation (http://wiki.ros.org/apriltag_ros). 
Aruco has been implemented in OpenCV, so it easier to use and have a broader feature support and integrate into devices more straightforward.
