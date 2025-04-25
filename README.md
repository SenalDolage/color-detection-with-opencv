# Color Detection with Open CV
A simple Python script that detects a specific color (e.g., yellow) in a live webcam feed and draws a bounding box around it using OpenCV.

Steps:
1. Capture Webcam Feed – Uses OpenCV to get live frames.

2. Convert to HSV – Better for color segmentation than RGB/BGR.

3. Generate Mask – Creates a binary image where the target color appears as a white blob.

4. Find Bounding Box – Locates the largest detected object.

5. Draw Rectangle – Visualizes the detection.

## Result

[![result.png](https://i.postimg.cc/Nfsd9808/result.png)](https://postimg.cc/XXPftCdX)

## Dependencies 

#### `pip install opencv-python Pillow numpy`
