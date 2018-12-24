title: Depth Image Segmentation Using Statistical Methods
date: 2016-01-10
author: Connor Monahan

Paper presented to the Junior Science, Engineering, and Humanities Symposium at Maryville University in 2016.

Abstract:

This paper presents an algorithm that utilizes unsupervised machine learning methods for
classifying n-objects in a spatial image. Other methods of spatial image segmentation, for
example the Laplacian operator and support vector machines (SVM), solely return all visible
edges within the image, which can then be used to find all objects within the frame; however,
this algorithm returns all points belonging to a specific object in the image rather than the edges
of the entire image. This allows the omission of further processing and categorizes all the present
data into classes using a modification of the Otsu thresholding method, by using a spatial metric
and optimizing the local minimum to the partial derivative of an n-modal distribution.
Implementation of the algorithm can be specialized to work on any list of points, such as an
entire image or a region of an image. The results of the algorithm return distinct information for
each object in the image, allowing further processing to determine other characteristics about the
object, such as the orientation.

Cite:

```
{% raw %}
@article{monahan2016,
title = {Depth Image Segmentation Using Statistical Methods},
author = {Monahan, Connor},
note = {preprint on webpage at \url{connormonahan.net}},
year = {2016}
}
{% endraw %}
```

[Article (PDF)]({static}/pdfs/Depth-Image-Segmentation-Using-Statistical-Methods.pdf)
