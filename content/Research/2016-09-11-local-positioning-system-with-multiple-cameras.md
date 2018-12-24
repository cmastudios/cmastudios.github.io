---
id: 16
title: Local Positioning System with Multiple Cameras
date: 2014-03-01T21:56:43+00:00
author: Connor Monahan
layout: post
guid: https://connormonahan.net/?p=16
permalink: /2016/09/11/local-positioning-system-with-multiple-cameras/
---
Paper presented to the Junior Science, Engineering, and Humanities Symposium at Maryville University in 2015.

Abstract:

This paper presents the process of obtaining, filtering, and tracking targets to obtain the
camera’s relative position. The program used computer specific architecture features to optimize
the program and provide consistent results immediately. First, images are obtained of the
environment from 3 different infrared cameras in gray-scale with a field of view of 120 degrees.
Next, the images underwent a series of image processing algorithms using the OpenCV
programming libraries, such as morphological transformations and binary topological analysis, to
identify the targets in the image. This converts the 1080p 1-channel matrix into a vector of points
called contours. A series of tests were then used to remove potential noise and error from the
data. The program then uses vectors and matrices as storage for calculating the positioning and
distance. At this point the information from each camera was combined and utilized in a GPS
style calculation was used to find the local position of the robot relative to the field. Finally, this
information was used to solve for the relative pose of the robot by solving a system of non-linear
functions. The results provide positioning and motion information of the robot relative to the
static environment.

Citation:

```
@article{monahan2015,
title = {Local Positioning System with Multiple Cameras},
author = {Monahan, Connor},
note = {preprint on webpage at \url{connormonahan.net}},
year = {2015}
}
```
[Article (PDF)]({static}/pdfs/Local-Positioning-System-with-Multiple-Cameras.pdf)
