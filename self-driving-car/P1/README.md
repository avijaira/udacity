# **Finding Lane Lines on the Road**
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />

Overview
---

When we drive, we use our eyes to decide where to go.  The lines on the road that show us where the lanes are act as our constant reference for where to steer the vehicle.  Naturally, one of the first things we would like to do in developing a self-driving car is to automatically detect lane lines using an algorithm.

In this project you will detect lane lines in images using Python and OpenCV.  OpenCV means "Open-Source Computer Vision", which is a package that has many useful tools for analyzing images.

Reflection
---

### 1. Pipeline overview

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I detect edges in the images using Canny algorithm, then I apply a polygon shaped image mask to the images, then I apply Hough Transform to detect straight lines within the region of interest in the images and draw only left and right lane lines, then I make the left and right lane lines drawn on the images semi-transparent.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by dividing up the straight lines detected by Hough Transform using their slope, within a range, into Left and Right lane lines. In addition, I calculate average slopes and average center points for both Left and Right lane lines. Now for each lane line, find the coordinates for start and end of the lines, using specified height values (y), average slope values, and average center points, calculate width values (x).

```
x = x' + (y - y') / M
    where:
        (x', y') are coordinates of average center point
        M is average slope
```

Once you have start point (lx1, ly1) and end point (lx2, ly2) for Left Lane, and start point (rx1, ry1) and end point (rx2, ry2) for Right Lane, draw them.

Here is an original test image:

![solidWhiteCurve (Original)](./test_images/solidWhiteCurve.jpg "solidWhiteCurve.jpg (Original)")

Here is same test image with lines drawn on it:
![solidWhiteCurve (with Lines)](./test_images_output/solidWhiteCurve.jpg "solidWhiteCurve.jpg (with Lines)")

### 2. Potential shortcomings with my current pipeline

One potential shortcoming would be what would happen when the lanes are curved (or sharp turns on the road), and the car is not driving in the middle of a lane, then the polygon shaped image mask defined would not fit well.

Another shortcoming could be the thresholds set for Right and Left Lane slopes. When the lanes are curved, the single lines drawn on the left and right lanes can't be straight lines, they should be curved as well.


### 3. Possible improvements to my current pipeline

A possible improvement would be to select a dynamic polygon shaped image mask, both in size and shape.

Another potential improvement could be to draw lines using a 2nd order polynomial, instead of a 1st order polynomial.
