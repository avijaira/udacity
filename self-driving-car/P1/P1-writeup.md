# **Finding Lane Lines on the Road**

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

---

### Reflection

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

