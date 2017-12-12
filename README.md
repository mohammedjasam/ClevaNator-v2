# ClevaNator-v2

This project is the iteration of the earlier project, it focuses on Object Detection rather that Image Classification like its predecessor. The Project is custom trained to detect violent actions in the video in Real-Time.

## Dependencies:
- Tensorflow
- Protoc-Compiler
- OpenCV 3
- Twilio API


## Installation:
- Go to modes/research/object_detection and run git pull
- Run protoc modes/research/object_detection/protos/* .proto --python_out=. (There is no space after * in the command)





- Config file:
> https://github.com/tensorflow/models/blob/master/research/object_detection/samples/configs/ssd_mobilenet_v1_pets.config

- Weights:
> Download the ssd_mobilenet_v1_coco_<timestamp>.tar.gz weight from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
