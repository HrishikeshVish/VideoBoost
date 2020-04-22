# VideoBoost
A GAN based neural network to improve the resolution of videos

## The Process
  1. Creation of Frames - OpenCV is used to extract the frames from a video. The number of frames in a lower quality video differs from that of the higher quality one and therefore, the 720p video is used to generate both the high resolution output and the low resolution input. A resize function is used to reduce the resolution to fit a 144p video. These frames form the input. 
  2. Creating the input dataset for the model - The frames are loaded using the functions defined in the keras.preprocessing library. Input and output images are stored in a numpy array. These two arrays are compressed and stored on the disk as a single .npz file. The images are resized to 256x256x3 to save storage space. 
  3. The GAN is trained with the input and the output images and the model is stored as a .h5 file
  4. Images of various videos can be loaded and the saved weights of the trained model are used to generate synthetic 720p images
  5. The synthetic images are resized to 1280x720x3 and stored on the disk
  6. Contrast, brightness and other properties are tweaked to improve the quality of the output
