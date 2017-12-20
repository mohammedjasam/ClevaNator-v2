# ClevaNator-v2

This project is the iteration of the earlier project, it focuses on Object Detection rather that Image Classification like its predecessor. The Project is custom trained to detect violent actions in the video in Real-Time.

## Dependencies:
- Tensorflow
- Protoc-Compiler
- OpenCV 3
- Twilio API
- Glob

## Installation:
### Tensorflow
- Open Command Prompt in admin mode.
- Type pip install tensorflow
- This command should download all the necessary packages to successfully install tensorflow on your system.

## Execution
### Training the Model:
- The model can be custom trained with your own set of classes; to do this, first gather the image dataset and place them in a folder named trainData and place that folder in ClevaNator-v2/violent_predictor/tf_files
- After placing the dataset in the right folder, execute the following command

  python35 -m tensorflow-for-poets-2.scripts.retrain
  --bottleneck_dir=tf_files/bottlenecks
  --how_many_training_steps=5000
  --model_dir=tf_files/models/
  --summaries_dir=tf_files/training_summaries/"mobilenet_0.50_224"
  --output_graph=tf_files/retrained_graph.pb
  --output_labels=tf_files/retrained_labels.txt
  --architecture="mobilenet_0.50_224"
  --image_dir=tf_files/trainData


### Predicting output from webcam:
- Navigate to ClevaNator-v2/violent_predictor/Video_Logger/
- Execute the command

  python record_vid_from_webcam.py

- Record the necessary video and press q to quit the webcam recording.
- This will record the video and generate frames in the folder generated_frames
- Now that you have the frames, execute the command

  python -m tensorflow-for-poets-2.scripts.label_image
  --graph=tf_files/retrained_graph.pb
  --image=path to /ClevaNatorv2/violent_predictor/Video_Logger/generated_frames/

### Predicting output from frames generated from a video:
- Navigate to ClevaNator-v2/violent_predictor/TestData
- Place the video which you want to predict in that folder (video_filename is the name of the video that you’ve just placed in the folder TestData)
- Execute the command

  python generate_frames_from_the_video.py video_filename

- This will generate the frames in the folder test
- Now that you have the frames, execute the command

 python -m tensorflow-for-poets-2.scripts.label_image
  --graph=tf_files/retrained_graph.pb
  --image=path to /ClevaNator-v2/violent_predictor/TestData/test/
