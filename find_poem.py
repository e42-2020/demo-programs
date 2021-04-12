# Create the screenshot images of the input.mp4
# for every 15 secs using this command
#
# > ffmpeg -i input.mp4 -vf fps=1/15 img%03d.jpg
#
# then run this program, to get the images, where
# poems are written


import os
# from skimage.measure import compare_ssimp
import matplotlib.pyplot as plt
import numpy as np
import cv2


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the sum of the squared difference between the two images
    mse_error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    mse_error /= float(imageA.shape[0] * imageA.shape[1])

 # return the MSE. The lower the error, the more "similar" the two images are.
    return mse_error


files = os.listdir()

files.sort()
# print(files)

prev_image = cv2.imread(files[1])
for i in range(2, len(files)-2):
    current_image = cv2.imread(files[i])
    # print(prev_image, current_image)
    # value = compare_ssim(prev_image, current_image)
    # print(value)
    # print(files[i], mse(prev_image, current_image))
    if mse(prev_image, current_image) < 50:
        print(files[i], mse(prev_image, current_image))
    prev_image = current_image
