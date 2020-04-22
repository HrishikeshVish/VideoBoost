# example of loading a pix2pix model and using it for image to image translation
from numpy import load
from numpy import vstack
from numpy.random import randint
from keras.models import load_model
from matplotlib import pyplot
import cv2 
# load and prepare training images
def load_real_samples(filename):
	# load compressed arrays
	data = load(filename)
	# unpack arrays
	X1, X2 = data['arr_0'], data['arr_1']
	# scale from [0,255] to [-1,1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]
 
# plot source, generated and target images
def plot_images(src_img, gen_img, tar_img):
	images = vstack((src_img, gen_img, tar_img))
	# scale from [-1,1] to [0,1]
	images = (images + 1) / 2.0
	titles = ['Source', 'Generated', 'Expected']
	# plot images row by row
	for i in range(len(images)):
		# define subplot
		pyplot.subplot(1, 3, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(images[i])
		# show title
		pyplot.title(titles[i])
	pyplot.show()
 
# load dataset
[X1, X2] = load_real_samples('image_data1.npz')
print('Loaded', X1.shape, X2.shape)
# load model
model = load_model('model_013000.h5')
src_image=X1
tar_image = X2
gen_images = model.predict(src_image)
count =0
for i in gen_images:
        i = cv2.resize(i, (1280,720), interpolation=cv2.INTER_AREA)
        i = (1/(2*2.25)) * i + 0.5
        #i = i/255
        pyplot.imsave("C:\\Users\\hrish\\Downloads\\VideoBoost\\output\\"+str(count)+".jpg", i)
        
        #cv2.imwrite("C:\\Users\\hrish\\Downloads\\VideoBoost\\output\\"+str(count)+".jpg",i)
        count+=1
"""
for i in range(100):
	# select random example
	ix = randint(0, len(X1), 1)
	src_image, tar_image = X1[ix], X2[ix]
	# generate image from source
	gen_image = model.predict(src_image)
	# plot all three images
	#plot_images(src_image, gen_image, tar_image)
"""
