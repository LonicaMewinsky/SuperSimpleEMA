#Super simple exponential moving average application to images
#No license; for demonstration purposes
import os
import numpy as np
import cv2
from PIL import Image

# Set the path for the input and output directories
input_dir = "C:/Users/spez/desktop/images/in"
output_dir = "C:/Users/spez/desktop/images/out"
# Set the strength here or at function call
ema_strength = 0.5

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Exponential moving average EMA "deflicker"
def deflicker(images, strength=ema_strength):
    #Make an array out of all of 'em
    image_array = np.array(images)

    #Seed the sequence with the first frame
    working_image = image_array[0].astype(np.float32)

    #Employ exponential moving average (EMA)
    return_images = []
    for i in range(len(images)):
        input_image = image_array[i].astype(np.float32)
        cv2.accumulateWeighted(input_image, working_image, strength)
        finished_out = cv2.convertScaleAbs(working_image)
        return_images.append(Image.fromarray(finished_out))
    
    return return_images

# Loop over the input directory and convert jpgs and pngs to np arrays
npimages = []
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image using PIL and convert it to a numpy array
        npimages.append(np.array(Image.open(os.path.join(input_dir, filename))))

# Convert all images using the above "deflicker" function
emaimages = deflicker(npimages)
for i in range(len(emaimages)):
    emaimages[i].save(os.path.join(output_dir, f"Frame_{'%0.6d' % i}.png"))