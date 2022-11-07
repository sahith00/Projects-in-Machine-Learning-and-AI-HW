import numpy as np
from skimage.io import ImageCollection, imread
from skimage.transform import resize

IM_HEIGHT = 64
IM_WIDTH = 64

def imread_resize(img):
    return resize(imread(img), (IM_HEIGHT, IM_WIDTH), anti_aliasing=True)

simpsons = ImageCollection('simpsons_dataset/*.jpg', load_func=imread_resize)

print("Created image collection")

np.save('simpsons_data.npy', np.asarray(simpsons))