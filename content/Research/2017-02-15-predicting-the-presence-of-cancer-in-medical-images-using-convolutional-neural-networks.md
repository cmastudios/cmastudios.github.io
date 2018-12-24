---
id: 67
title: Predicting the Presence of Cancer in Medical Images using Convolutional Neural Networks
date: 2017-02-15T22:43:21+00:00
author: Connor Monahan
layout: post
guid: https://connormonahan.net/?p=67
permalink: /2017/02/15/predicting-the-presence-of-cancer-in-medical-images-using-convolutional-neural-networks/
---
Paper submitted to Missouri Junior Science, Engineering, and Humanities Symposium for 2017

Abstract:

Convolutional neural networks model human brain activity from sensory inputs and have been applied to various activities such as driving cars, recognizing speech, and playing complex games. These machine learning algorithms gained popularity in recent years as an effective method for pattern recognition. This paper proposes a novel convolutional neural network architecture to detect lung cancer in radiographic images. Given that patients routinely have x-rays taken for pre-emptive health screenings, and the growing amount of medical data from these imaging procedures, the need for automated detections of abnormalities increases. The solution used a dataset of labeled x-ray images of patients with confirmed instances of lung cancer combined with an equal set of cancer-free patients. The network relied on rectified linear unit activations and dropout to reduce overfitting. Then, this neural network model was trained with a standard backpropagation algorithm with an Adam optimizer using softmax regression. This model demonstrated a 91% accuracy rate on lung cancer chest x-rays.

Cite:

```
@article{monahan2017,
title = {Predicting the Presence of Cancer in Medical Images using Convolutional Neural Networks},
author = {Monahan, Connor},
note = {preprint on webpage at \url{connormonahan.net}},
year = {2017}
}
```
[Article (PDF)]({static}/pdfs/Predicting-the-Presence-of-Cancer-in-Medical-Images-using-Convolutional-Neural-Networks.pdf)
