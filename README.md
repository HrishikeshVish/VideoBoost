# VideoBoost
A GAN based neural network to improve the resolution of videos
#### Hrishikesh V (hrishi.vish@outlook.com)

## AIM
The primary goal of this project is to find a way to improve the resolution of videos using a machine learning technique to generate high resolution videos from a low resolution one. 

## Generative Adversarial Network
The Generative Adversarial Network is a set of two neural networks which are pitted against each other simulating a minimax game. The first network, or the descriminator learns to discern between real high quality images and synthetic high quality images. It is first trained independantly, with a large set of real 720p images. The weights are then preserved. 

The Generator is an autoencoder comprising an encoder connected to a decoder. The encoder processes the low resolution image and the decoder generates a high resolution image from the input fed to the encoder. The output is passed to the discriminator which by then knows what real images look like. 

The Generator improves it's performance by trying to create images as close to the real ones as possible. Training ends when the discriminator is unable to differentiate between real and synthetic images. The Generator by then has learnt the weights to create a high resolution frame from a low resolution frame. 

## The Process
  1. *Creation of Frames* - OpenCV is used to extract the frames from a video. The number of frames in a lower quality video differs from that of the higher quality one and therefore, the 720p video is used to generate both the high resolution output and the low resolution input. A resize function is used to reduce the resolution to fit a 144p video. These frames form the input. 
  2. *Creating the input dataset for the model* - The frames are loaded using the functions defined in the keras.preprocessing library. Input and output images are stored in a numpy array. These two arrays are compressed and stored on the disk as a single .npz file. The images are resized to 256x256x3 to save storage space. 
  3. *Training the Model* - The GAN is trained with the input and the output images and the model is stored as a .h5 file
  4. *Testing* - Images of various videos can be loaded and the saved weights of the trained model are used to generate synthetic 720p images
  5. *Resizing* - The synthetic images are resized to 1280x720x3 and stored on the disk
  6. *Image Processing* - Contrast, brightness and other properties are tweaked to improve the quality of the output

## Output
### Case 1
#### Input
#### Actual Output
#### Expected

### Case 2
#### Input
#### Actual Output
#### Expected

### Case 3
#### Input
#### Actual Output
#### Expected

### Case 4
#### Input
#### Actual Output
#### Expected

### Case 5
#### Input
#### Actual Output
#### Expected

### Case 6
#### Input
#### Actual Output
#### Expected
