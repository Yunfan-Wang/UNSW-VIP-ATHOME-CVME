## Experiments

These experiments are done to gain a better understanding of the semantics and performance of state-of-the-art computer vision algorithms.

#### `detectron2_test.py`

Based on the [detectron2](https://github.com/facebookresearch/detectron2) package. This program takes an image or video as input and performs one of the 4 computer vision tasks. Supported tasks include: 

- object detection: locate and identify instances of objects in an image.
![Alt text](image.png)
- instance segmentation: locate and identify instances of objects in an image, then demarcate these objects by identifying their boundaries.
![Alt text](image-1.png)
- keypoint detection: localising key points of the human body like joints, shoulders, hips etc.
![Alt text](image-2.png)
- panoptic segmentation: combines semantic segmentation with instance segmentation.
![Alt text](image-3.png)

#### `manydepth_test.py`
Based on the [manydepth](https://github.com/nianticlabs/manydepth) package. This program takes an image or video as input and performs self-supervised monocular depth estimation.

![Alt text](image-5.png)

#### `corner_detection_test.py`
This program uses OpenCV Harris corner detection to detect corners in a given image. Users are able to configure the detection threshold to suit the needs of different images and directly preview the result.

![Alt text](image-4.png)